import socket

# 建立socket链接 基于网络套接字家族:AF_INET tcp协议：SOCK_STREAM
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 与服务端（ip+port）建立链接
tcp_client.connect(("127.0.0.1", 5050))
while True:
    msg = input(">>:").strip()  # 排除发送无效的空格符
    # 给服务端发消息
    if msg:  # 判断是否有请求信息（排除回车等空请求造成阻塞）
        tcp_client.send(msg.encode("utf-8"))
        # 接收服务端的消息
        data = tcp_client.recv(1024)
        if data.decode("utf-8") == "exit":  # 如果服务端返回exit 退出循环，断开连接
            print("与服务端断开连接....")
            break
        print("服务端说：", data.decode("utf-8"))
# 关闭与服务端的链接
tcp_client.close()