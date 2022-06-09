from socket import *

ip_port = ("127.0.0.1", 5030)
buf_size = 2048

# 创建socket连接
cmd_client = socket(AF_INET, SOCK_DGRAM)

# 实现通信循环
while True:
    cmd_msg = input(">>:").strip()
    if not cmd_msg:
        continue

    # 如果发送exit，中断连接
    if cmd_msg == "exit":
        break

    # 发送指令给服务端
    cmd_client.sendto(cmd_msg.encode("utf-8"), ip_port)
    # 接收服务端数据
    data, add = cmd_client.recvfrom(buf_size)
    print(data.decode("gbk"))

# 关闭连接
cmd_client.close()