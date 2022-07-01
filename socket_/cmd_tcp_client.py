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
    # buffer = b'admin'
    # sendall(buffer)  # 尝试发送string的所有数据，成功则返回None，失败则抛出异常
    # =
    # while buffer:
    #     len = send(buffer)  # send()的返回值是发送的字节数量，这个数量值可能小于要发送的string的字节数，也就是说可能无法发送string中所有的数据。如果有错误则会抛出异常
    #     buffer = buffer[len:]
    len = cmd_client.send(cmd_msg.encode("utf-8"))
    print("len,ok:", len)
    # 接收服务端数据
    data = cmd_client.recv(200)
    print(data.decode("gbk"))

# 关闭连接
cmd_client.close()