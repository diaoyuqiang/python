from threading import Timer
import time


def run(n):
    print("hello %s" % n)
    print(time.time() - time1)


t = Timer(5, run, (2,))  # 线程定时器, Thread衍生类
time1 = time.time()
t.start()
# t.cancel()  # 在等待时间内可以取消执行
