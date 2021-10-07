import socketserver


class MyHandler(socketserver.BaseRequestHandler):

    def handle(self):
        udp = self.request[1]  # 服务端
        # print(self.request, type(self.request))  # request是一个元祖，[0]为data
        data = self.request[0]  # 客户端发来的消息
        # 如果消息为空，关闭服务端
        # if not data:
        #     self.server.shutdown()  # 关闭服务端

        # 如果exit，中断连接
        if data.decode() == "exit":
            udp.sendto(data, self.client_address)
            return
        # 发消息给客户端
        udp.sendto(data.upper(), self.client_address)  # self.client_address 为客户端地址


if __name__ == "__main__":

    server = socketserver.ThreadingUDPServer(("127.0.0.1", 5070), MyHandler)
    server.serve_forever()  # 实现通信循环