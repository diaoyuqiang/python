import threading
import time


def add():
    global num
    lock.acquire()  # 加锁
    print("num:", num)
    temp = num
    num = temp + 1
    lock.wait(2)  # 线程等待,阻塞线程直到收到一个notify或者超时后会被唤醒
    lock.notify()  # 通知其他线程执行
    # lock.notify_all()  # 通知其他所有线程执行
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
    lock = threading.Condition()  # 创建等待条件
    for i in range(2):
        t = threading.Thread(target=add)
        t1 = threading.Thread(target=sub)
        t.start()
        t1.start()

    time.sleep(3)
    print(num, _sub)