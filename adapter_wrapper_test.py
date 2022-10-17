#!/usr/bin/env python
# -*- coding: utf-8 -*-
class adaptee(object):
    def foo(self):
        print('foo in adaptee')
    def bar(self):
        print('bar in adaptee')

# 组合属性适配器
class adapter(object):
    def __init__(self):
        self.adaptee = adaptee()

    def foo(self):
        print('foo in adapter')
        # self.adaptee.foo()

    def __getattr__(self, name):  # __getattr__: 实例属性查找的最后一步
        print('name',name)
        return getattr(self.adaptee, name)

if __name__ == '__main__':
    a = adapter()
    a.foo()
    a.bar()