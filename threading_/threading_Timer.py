from threading import Timer
import time


def run(n):
    print("hello %s" % n)


t = Timer(5, run, (2,))  # 定时器， Thread衍生类
time1 = time.time()
t.start()
# t.cancel()  # 在等待时间内可以取消执行
print(time.time()-time1)