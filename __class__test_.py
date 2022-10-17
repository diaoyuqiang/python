#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A(object):
    count = 0

    def __init__(self):
        self.__class__.count += 1  # __class_: 返回实例的类，再通过类调用类属性


print(A.count)
a = A()
print(a)
print(a.count)
b = A()
print(b)
print(b.count)
print(a.count)  # 实例直接调用类属性