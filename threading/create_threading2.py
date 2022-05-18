import threading
import time
import gevent


class MyThread1(threading.Thread):

    def __init__(self, num):
        threading.Thread.__init__(self)  # 重写必须调用Thread的__init__方法
        self.num = num

    def hi(self):
        print('tree %d' % self.num)
        time.sleep(10)
        print("target")

    def run(self):
        self.hi()

class MyThread(threading.Thread):

    def __init__(self, num):
        threading.Thread.__init__(self)  # 重写必须调用Thread的__init__方法
        self.num = num

    def hi(self):
        print('hello %d' % self.num)
        # time.sleep(0.9)
        print("ending")
        
    def run(self):
        self.hi()


if __name__ == '__main__':
    tm1 = time.time()

    t = MyThread(10)  # 创建子线程
    t.start()

    t1 = MyThread1(5)  # 创建子线程
    t1.start()

    print('我是主线程..')
    # t.join()
    # t1.join()
    # tm2 = time.time() - tm1
    # print("tm2:", tm2)