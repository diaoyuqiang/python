import socket
import threading

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(('127.0.0.1', 6001))

tcp_server.listen(5)


def start(con):
    while True:
        data = con.recv(1024)
        print(data.decode())
        con.send(data)


if __name__ == '__main__':
    while True:
        con, add = tcp_server.accept()
        t = threading.Thread(target=start, args=(con,))  # 创建tcp连接的线程对象
        t.start()


