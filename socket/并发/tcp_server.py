import socketserver  # 并发模块


class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("conn 是：", self.request)  # conn
        print("add 是：", self.client_address)  # add

        while True:  # 实现通信循环
            try:
                data = self.request.recv(1024)
                if not data:
                    break
                # 判断是否是指定的字符串，与客户端断开连接
                if 'exit' == data.decode():
                    self.request.sendall(data)
                    self.request.close()
                    break

                data = data.decode()
                print("客户端的消息：", data, self.client_address)  # 内容+地址
                # 将接收到的消息转化成大写发送
                self.request.sendall(data.upper().encode())

            except Exception as e:
                print(e)
                break

        # self.server.shutdown()  # 关闭链接循环


if __name__ == "__main__":

    server = socketserver.ThreadingTCPServer(("127.0.0.1", 5050), MyHandler)  # 创建tcp多线程对象
    server.serve_forever()  # 实现链接循环