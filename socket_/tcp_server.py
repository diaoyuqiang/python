import socket

# 建立socket链接 基于网络套接字家族:AF_INET tcp协议：SOCK_STREAM
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定服务端的ip+port
tcp_server.bind(("127.0.0.1", 5006))
# 声明最大连接数
tcp_server.listen(10)  # 监听
# 得到一个持续的链接和客户端地址
conn, addr = tcp_server.accept()  # 三次握手
print(conn, addr)
# 接收客户端的消息（字节码）
data = conn.recv(1024)  # 缓冲大小1024
print(data.decode("utf-8"))
# 发送消息给客户端
conn.send("服务端消息...".encode("utf-8"))
# 关闭链接
conn.close()  # 四次挥手
# 关闭服务端
tcp_server.close()
