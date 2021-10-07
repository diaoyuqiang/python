import time
import random
import grpc
import hello_bilbil_pb2 as pd
import hello_bilbil_pb2_grpc as pd_grpc

def test():
    index = 0
    while True:
        time.sleep(1)
        data = str(random.random())
        if index == 5:
            break
        print(index)
        index += 1
        yield pd.TestTwoWaysReq(data=data)


def run():
    conn = grpc.insecure_channel("127.0.0.1:5000")  # 定义客户端频道并绑定ip端口
    client = pd_grpc.BilbilStub(channel=conn)  # 定义客户端
    try:
        response, call = client.HelloDyq.with_call(pd.HelloDyqReq(  # 写入请求参数，并接收返回数据, call接收metadata数据
            name="dyq",
            age=18
        ), compression=grpc.Compression.Gzip, metadata=(("name", "dyq"),), wait_for_ready=True)  # 客户端发送压缩数据、metadata数据
        print(response.result)
        headers = call.trailing_metadata()
        print(headers[0].key, headers[0].value)  # 取第一个元祖中的key和value的值
        # print(call.trailing_metadata())  # 打印服务端返回的metadata数据
    except Exception as e:  # 捕获异常
        print(e.code().value[0], ":", e.details())
    # response = client.HelloBoyCli(pd.HelloBoyCliReq(
    #     data="DYQ"
    # ))
    #
    # for item in response:
    #     print(item.result)

    # print(response.result)  # 输出返回结果

    # response = client.HelloSend(test())
    # print(response.result)

    # response = client.TestTwoWays(test(), timeout=60)
    # for res in response:
    #     print(res.result)


if __name__ == "__main__":
    run()
