#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal:
    def __del__(self):
        print("调用父类 __del__() 方法")


class Bird(Animal):
    def __del__(self):
        # super(Bird,self).__del__()  #方法1：显示调用父类的del方法
        print("调用子类 __del__() 方法")


cat = Bird()
# del cat   #只能调用子类里面的__del__
"""
重写子类的del()方法，则必须显式调用父类的del()方法，这样才能保证在回收子类对象时，其占用的资源（可能包含继承自父类的部分资源）能被彻底释放。
"""
super(Bird, cat).__del__() #方法2：显示调用父类的__del__
