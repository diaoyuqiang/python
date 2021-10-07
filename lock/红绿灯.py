import threading
import time

"""
三个对象 街道 人 车
街道有两个方法：1.车走人停 2.人走车停 
街道负责通知人或者车谁走--具有condition的能力
人和车有线程start的能力
"""


class Street(object):
    def __init__(self, condition):

        # True 人走车停 南北向
        # False 车走人停 东西向
        self.flag = True
        self.condition = condition

    def south_north(self):
        while True:
            self.condition.acquire()  # 加锁
            # 人停
            if not self.flag:
                self.condition.wait()  # 线程等待
            # 人走
            print('人走南北向...', threading.current_thread().name)  # 获取当前线程名称
            time.sleep(2)
            # 变灯
            self.flag = not self.flag
            # 通知车走
            self.condition.notify()
            self.condition.release()

    def east_west(self):
        while True:
            self.condition.acquire()  # 加锁
            # 车停
            if self.flag:
                self.condition.wait()  # 线程等待
            # 车走
            print('车走东西向...', threading.current_thread().name)
            time.sleep(1)
            # 变灯
            self.flag = not self.flag
            # 通知人走
            self.condition.notify()
            self.condition.release()


# 人
class Person(threading.Thread):

    def __init__(self, street, name):
        self.street = street
        super().__init__(name=name)  # 修改线程名称

    def run(self):
        self.street.south_north()  # 人开始走


# 车
class Car(threading.Thread):
    def __init__(self, street, name):
        self.street = street
        super().__init__(name=name)  # 修改线程名称

    def run(self):

        self.street.east_west()  # 车开始走


if __name__ == '__main__':

    s = Street(threading.Condition())  # 传入互斥锁对象
    p = Person(s, 'person')
    p.start()

    c = Car(s, 'car')
    c.start()