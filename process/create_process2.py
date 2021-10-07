from multiprocessing import Process


class MyThread(Process):

    def __init__(self, num):
        super().__init__()  # 重写必须调用Process的__init__方法
        self.num = num

    def hi(self):
        print('hello %d' % self.num)

    # 进程执行方法
    def run(self):
        self.hi()


# 进程并行
if __name__ == '__main__':
    t = MyThread(10)  # 创建子进程
    t.start()

    t1 = MyThread(5)  # 创建子进程
    t1.start()

    print('我是主进程..')