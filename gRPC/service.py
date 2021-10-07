import time
import grpc
import hello_bilbil_pb2 as pd
import hello_bilbil_pb2_grpc as pd_grpc
from concurrent import futures  # 从并发模块导入futures

# 客户端与服务端互相传输heads：key,values  也就是指metadata(元数据)
# 客户端与服务端传输数据、接收数据 进行压缩与解压缩
# 服务端书写拦截器类(验证客户端请求或者记录留痕)  code detail
# 拦截器函数 grpc_code 错误函数 abort  intercept_service(self, continuation, header_call_details)


def _abort(code, details):  # 拦截器返回的错误信息
    def terminate(ignored_request, context):  # unary stream
        context.abort(code, details)
    return grpc.unary_unary_rpc_method_handler(terminate)  # 返回闭包函数


class TestInterceptor(grpc.ServerInterceptor):  # 服务端拦截器类
    def __init__(self, key, value, code, detail):  # 初始化函数
        self.key = key
        self.value = value
        self._abort = _abort(code, detail)

    def intercept_service(self, continuation, handler_call_details):  # 拦截服务函数
        # continuation 函数执行器  handler_call_details 请求的元数据
        headers = dict(handler_call_details.invocation_metadata)  # metadata元祖转换成字典
        if headers.get(self.key, "") != self.value:
            return self._abort
        # if (self.key, self.value) not in handler_call_details.invocation_metadata:
        #     return self._abort
        return continuation(handler_call_details)


class Bilbil(pd_grpc.BilbilServicer):
    def HelloDyq(self, request, context):
        name = request.name
        age = request.age
        # context.set_details("is bug")  # 错误信息
        # context.set_code(grpc.StatusCode.DATA_LOSS)  # 错误代码
        # raise context  # 抛出异常错误

        context.set_trailing_metadata((("name", "dyq"), ("key", "values")))  # 发送metadata数据
        headers = context.invocation_metadata()
        print(headers[0].key, headers[0].value)  # 服务端接收客户端请求的metadata数据
        # context.set_compression(grpc.Compression.Deflate)  # HelloDyq函数向客户端发送压缩数据
        result = f"my name is {name}, my age is {age}"
        return pd.HelloDyqReply(result=result)

    def HelloBoyCli(self, request, context):
        index = 0
        while context.is_active():  # 检测客户端是否在线
            data = request.data  # 客户端请求数据
            if data == "close":  # 如果data等于"close"
                print("data is close request will close!")
                context.cancle()  # 关闭服务端与客户端的长连接
            time.sleep(1)
            index += 1
            # result = "1"
            result = "send %s %d" % (data, index)
            print(result)
            yield pd.HelloBoyCliReply(
                result=result  # 响应并返回result数据
            )

    def HelloSend(self, request_iterator, context):
        index = 0
        for request in request_iterator:
            print(request.data, ":", index)
            if index == 10:
                break
            index += 1
        return pd.HelloSendReply(result="ok")

    def TestTwoWays(self, request_iterator, context):  # 双向流
        for request in request_iterator:  # 服务端获取客户端请求流的数据
            data = request.data
            yield pd.TestTwoWaysResponse(result="service send to client %s" % data)  # 服务端向客户端返回响应的流数据


def run():
    validator = TestInterceptor("name", "dyq", grpc.StatusCode.UNAUTHENTICATED, "Access denied")  # 实例化拦截器对象
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=5),  # 最大工作线程数量
        compression=grpc.Compression.Gzip,  # 服务端向客户端发送压缩数据
        interceptors=(validator, ),  # 返回客户端拦截信息
        options=[
            ("grpc.max_send_message_length", 50 * 1024 * 1024),  # 服务端发送给客户端的最大数据量 50M  （服务端默认可接收2M）
            ("grpc.max_receive_message_length", 50 * 1024 * 1024)  # 服务端可接收客户端的最大数据 50M
        ]
    )

    pd_grpc.add_BilbilServicer_to_server(Bilbil(), grpc_server)  # 把Bilbil实例对象注册到grpc_server里
    grpc_server.add_insecure_port("127.0.0.1:5000")  #绑定ip端口
    print("service started in dyq")
    grpc_server.start()  # 启动服务

    try:
        while True:
            time.sleep(3600)  # 挂起服务进程 60min
    except KeyboardInterrupt:  # 捕获ctrl+c 终止按键操作
        grpc_server.stop(0)


if __name__ == "__main__":
    run()