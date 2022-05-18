import time
from threading import Thread

# 获取线程函数返回值的两种方法: 1.线程类定义获取函数; 2.放进队列里
# 自定义线程类
class Product(Thread):
    def __init__(self, num):
        Thread.__init__(self)  # 调用Thread.__init__的固定写法
        self.num = num

    def get_ret(self):
        return self.num
    # 启动函数
    def run(self):
       self.get_ret()


t = Product(1)
t.start()
t.join()
print(t.get_ret())  # 主线程捕获子线程返回的num



