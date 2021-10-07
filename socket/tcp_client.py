import socket

# 建立socket链接 基于网络套接字家族:AF_INET tcp协议：SOCK_STREAM
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 与服务端（ip+port）建立链接
tcp_client.connect(("127.0.0.1", 5006))
# 给服务端发消息
tcp_client.send("hello".encode("utf-8"))
# 接收服务端的消息
data = tcp_client.recv(1024)
print(data.decode("utf-8"))
# 关闭与服务端的链接
tcp_client.close()