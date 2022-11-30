#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Temp(object):
    a = 1
    b = 3


class A(Temp):
    def __init__(self):
        super(A, self).__dict__.update(a=12)  # 更新实例的__dict__

    def get_(self):
        return super(A, self).__dict__


a = A()
print(a.__dict__)
print(a.get_())
print(a.b)
print(a.a)
print(dir(a))

# print A.__dict__
