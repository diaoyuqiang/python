import socket

back_log = 10
buf_size = 1024
# 建立socket链接 基于网络套接字家族:AF_INET tcp协议：SOCK_STREAM
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定服务端的ip+port
tcp_server.bind(("127.0.0.1", 5007))
# 声明最大连接数
tcp_server.listen(back_log)  # 监听
# 外层循环,链接循环：保证服务端永久执行
while True:
    # 得到一个持续的链接和客户端地址
    conn, addr = tcp_server.accept()  # 三次握手
    print(conn, addr)
    # 内层/通信循环(实现与客户端的循环交互)
    while True:
        # 客户端强制中断连接，win会抛出异常给服务端
        # 客户端强制中断连接，linux会不断发送空给服务端
        try:
            # 接收客户端的消息（字节码）
            data = conn.recv(buf_size)  # 缓冲大小1024
            if not data:  # 请求数据为空，退出循环，断开连接
                break
            if data.decode("utf-8") == "exit":  # 接收客户端发送的exit，响应exit并退出循环，断开连接
                conn.send(data)
                break
            print(data.decode("utf-8"))
            # 发送消息给客户端
            msg = input(">>:")
            conn.send(msg.encode("utf-8"))
        except Exception as e:  # 捕获客户端连接异常
            print("异常信息为：", e)
            break
    # 关闭与客户端的链接
    conn.close()  # 四次挥手
# 关闭服务端
tcp_server.close()
