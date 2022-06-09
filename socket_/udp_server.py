from socket import *

buf_size = 1024
ip_port = ("127.0.0.1", 5010)

# 创建socket链接 基于AF_INET,UDP协议
udp_server = socket(AF_INET, SOCK_DGRAM)
# 绑定ip和port
udp_server.bind(ip_port)
while True:
    # 接收客户端请求数据（字节码、客户端ip+端口）
    data, add = udp_server.recvfrom(buf_size)
    print(data.decode(), add)
    # 发送数据到客户端
    udp_server.sendto("我是服务端....".encode("utf-8"), add)
# 关闭与客户端的连接
udp_server.close()