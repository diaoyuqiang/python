import threading
import time


def add():
    global num
    _lock.acquire()  # 加锁
    temp = num
    time.sleep(0.0001)
    num = temp + 1
    _lock.release()  # 释放锁


if __name__ == '__main__':
    num = 0
    l = []
    _lock = threading.Lock()  # 创建互斥锁对象
    for i in range(100):
        t = threading.Thread(target=add)
        t.start()
        l.append(t)

    for _ in l:
        _.join()

print(num)