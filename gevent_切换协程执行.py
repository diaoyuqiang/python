import gevent
import time


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)  # 获取当前的greenlet
        # time.sleep(0.5)
        gevent.sleep(0.5)


print("--------1---------")
g1 = gevent.spawn(f1, 5)  # 创建协程对象并执行
print("--------2---------")
g2 = gevent.spawn(f1, 5)
print("--------3---------")
g3 = gevent.spawn(f1, 5)
print("--------4---------")
g1.join()
g2.join()
g3.join()