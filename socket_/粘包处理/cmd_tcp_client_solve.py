from socket import *
import struct  # 封包，拆包

ip_port = ("127.0.0.1", 5020)
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
    cmd_client.send(cmd_msg.encode("utf-8"))
    # 接收服务端数据
    """
    解决粘包：
    """
    length_data = cmd_client.recv(4)   # 以4个字节长度读取封装过后的数据
    # print(length_data)
    # 拆包
    length = struct.unpack("i", length_data)[0]  # 返回的是一个元祖, [0]:为数据长度
    # print(length)

    recv_size = 0
    recv_msg = b''  # 字节码

    while recv_size < length:
        recv_msg += cmd_client.recv(1024)
        recv_size = len(recv_msg)

    print(recv_msg.decode("gbk"))

# 关闭连接
cmd_client.close()