import threading
import time


class MyThread(threading.Thread):

    def __init__(self, num):
        threading.Thread.__init__(self)  # 重写必须调用Thread的__init__方法
        self.num = num

    def hi(self):
        print('hello %d' % self.num)
        time.sleep(3)
        
    def run(self):
        self.hi()


if __name__ == '__main__':
    t = MyThread(10)  # 创建子线程
    t.start()

    t1 = MyThread(5)  # 创建子线程
    t1.start()

    print('我是主线程..')