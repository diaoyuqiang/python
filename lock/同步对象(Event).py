import threading
import time


class Boss(threading.Thread):
    def run(self):
        print("今晚加班到10:00..")
        _en.set()  # 将等待线程的状态改为True

        time.sleep(3)
        print("下班...")
        _en.set()


class Worker(threading.Thread):
    def run(self):
        print(_en.is_set())  # 查看同步对象的等待状态
        _en.wait()  # 设置等待线程 默认值为False
        print("哎，命苦...")
        print(_en.is_set())
        _en.clear()  # 清除设置过的等待状态
        _en.wait()
        print("happy...")


if __name__ == '__main__':
    _en = threading.Event()  # 同步对象
    a = Boss()
    b = Worker()

    b.start()
    a.start()
