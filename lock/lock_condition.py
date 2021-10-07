import threading
import time


def add():
    global num
    lock.acquire()  # 加锁
    print("num:", num)
    temp = num
    num = temp + 1
    lock.wait()  # 线程等待
    lock.notify()  # 通知其他线程执行
    lock.release()  # 释放锁


def sub():
    global _sub
    lock.acquire()
    print("_sub:", _sub)
    temp = _sub
    _sub = temp - 1
    lock.wait()
    lock.notify()
    lock.release()


if __name__ == '__main__':
    num = 0
    _sub = 100
    lock = threading.Condition()  # 创建同步锁对象
    for i in range(100):
        t = threading.Thread(target=add)
        t1 = threading.Thread(target=sub)
        t.start()
        t1.start()

    time.sleep(5)

    print(num, _sub)