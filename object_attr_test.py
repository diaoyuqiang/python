#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Mymeta(type):  # 继承type生成自定义元类
    def __init__(self, class_name, class_bases, class_dict):  # 类名，基类，类dict
        super().__init__(class_name, class_bases, class_dict)
        print(self.__base__)  # 查看基类

    def __get__(cls, instance, owner):  # 存在了__get__的方法的类称之为描述符类(descriptor), 作为其他类属性时调用
        print('this is %s' % cls, instance, owner)
        return 3



# 查找一个对象得属性顺序a.x -> a.__dict__['x'] -> type(a).__dict__['x'] -> type(a)
class A(object, metaclass=Mymeta):
    # pass
    def __get__(self, instance, owner):
        print('this is %s' % self, instance, owner) # obj A -> obj B -> class B
        return 5


class B(object):
    attr = A

    def __init__(self):
        self.name = 'test'

    def func1(self):
        print('haha')

    def func2(self):
        pass

b = B()
# print(B.__dict__)
# print(b.__dict__)  # 实例属性列表
# # <bound method B.func1 of <__main__.B object at 0x022ADFB0>> 类方法绑定到self实例中
# print(b.func1)
# print(B.func1)
# B.func1(B())
print(b.attr)
# print(type(A)) # 元类: <class 'type'>
# print(dir(b))