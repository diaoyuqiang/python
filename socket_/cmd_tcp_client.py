from socket import *

ip_port = ("127.0.0.1", 5020)
back_log = 5
buf_size = 1024

# 创建socket连接
cmd_client = socket(AF_INET, SOCK_STREAM)
# 建立连接
cmd_client.connect(ip_port)

# 实现通信循环
while True:
    cmd_msg = input(">>:").strip()
    if not cmd_msg:
        continue

    # 如果发送exit，中断连接
    if cmd_msg == "exit":
        break

    # 发送指令给服务端
    len = cmd_client.send(cmd_msg.encode("utf-8"))
    print("len,ok:", len)
    # 接收服务端数据
    data = cmd_client.recv(200)
    print(data.decode("gbk"))

# 关闭连接
cmd_client.close()