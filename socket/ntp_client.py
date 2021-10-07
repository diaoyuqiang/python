from socket import *

buf_size = 1024
ip_port = ("127.0.0.1", 5010)
# 创建socket链接 基于AF_INET,UDP协议
udp_client = socket(AF_INET, SOCK_DGRAM)
while True:
    # 客户端发送请求
    msg = input(">>:")
    udp_client.sendto(msg.encode("utf-8"), ip_port)
    # 接收服务端返回的数据
    data, add = udp_client.recvfrom(buf_size)
    print(data.decode())
# 关闭与服务端的连接
udp_client.close()