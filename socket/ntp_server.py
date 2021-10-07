from socket import *
import time

buf_size = 1024
ip_port = ("127.0.0.1", 5010)

# 创建socket链接 基于AF_INET,UDP协议
udp_server = socket(AF_INET, SOCK_DGRAM)
# 绑定ip和port
udp_server.bind(ip_port)
while True:
    # 接收客户端请求数据（字节码、客户端ip+端口）
    data, add = udp_server.recvfrom(buf_size)  # 返回的是元祖
    if not data:
        # 如果用户输入为空，返回默认的时间格式
        fmt = "%Y-%m-%d %X"
    else:
        # 如果用户输入了时间，返回相应的时间字符串
        fmt = data.decode("utf-8")

    # 发送数据到客户端
    msg = "ntp标准服务的时间是：" + time.strftime(fmt)
    udp_server.sendto(msg.encode("utf-8"), add)
# 关闭与客户端的连接
udp_server.close()