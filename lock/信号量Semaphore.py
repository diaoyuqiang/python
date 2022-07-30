import threading
import time


class MyThread(threading.Thread):
    def run(self):
        # if _lock.acquire():
        with _lock:
            print(self.name)
            time.sleep(2)
        # _lock.release()


if __name__ == '__main__':
    _lock = threading.Semaphore(5)  # 设置信号量对象(信号量主要是用来维持有限的资源，使得在一定时间使用该资源的线程只有指定的数量.)
    l = []
    for i in range(50):
        t = MyThread()
        t.start()
        l.append(t)