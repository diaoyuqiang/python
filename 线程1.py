import threading_
import time


def fun1(thread_name, delay):
    print('线程{}开始执行'.format(thread_name))
    time.sleep(delay)
    print('线程{}运行fun1结束'.format(thread_name))


def fun2(thread_name, delay):
    print('线程{}开始执行'.format(thread_name))
    time.sleep(delay)
    print('线程{}运行fun2结束'.format(thread_name))


if __name__ == '__main__':
    print("主进程执行")
    # 创建线程
    t1 = threading_.Thread(target=fun1, args=('thread1', 3))
    t2 = threading_.Thread(target=fun2, args=('thread2', 2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()