#coding=utf-8
from types import FunctionType
import functools

# 自定义元类
class Agv(type):  # 元类是由type衍生出来，所以需继承type

    def __new__(cls, future_class_name, parents, attrs, *args, **kwargs):  # future_class_name: 要创建类的名字, parents: 父类, attrs:类对象属性dict
        attrs['name'] = "dyq"
        for k, v in attrs.items():
            if isinstance(v, FunctionType):
                # v(cls)
                attrs[k] = exception_handle(v)  # 装饰器函数传入真实函数，返回闭包函数，将对象中的原函数替换为闭包函数
        return type.__new__(cls, future_class_name, parents, attrs, *args, **kwargs)

# 自动捕捉异常装饰器
def exception_handle(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print "捕获:{}".format(e)

    return inner

class Car():
    __metaclass__ = Agv

    def __init__(self):
        self.age = 20

    def run(self, a, b):
        c = a / b

c = Car()
c.run(1, 0)  # 被装饰的真实函数调用
print c.name