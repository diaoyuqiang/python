import threading
import time


class MyThread(threading.Thread):
    def run(self):
        if _lock.acquire():
            print(self.name)
            time.sleep(2)
        _lock.release()


if __name__ == '__main__':
    _lock = threading.Semaphore(5)  # 设置信号量对象
    l = []
    for i in range(100):
        t = MyThread()
        t.start()
        l.append(t)