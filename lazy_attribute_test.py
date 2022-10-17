#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

class lazy_attribute(object):
    """ A property that caches itself to the class object. """

    def __init__(self, func):
        functools.update_wrapper(self, func, updated=[])  # 把被封装函数的name、module、doc和 dict都复制到封装函数去
        self.getter = func

    def __get__(self, obj, cls):
        value = self.getter(cls)
        # print('self:', self)
        print('SELF.__dict__:', self.__dict__)
        setattr(cls, self.__name__, value)
        return value

class Widget(object):
    @lazy_attribute
    def complex_attr_may_not_need(cls):
        print('complex_attr_may_not_need is needed now')
        return sum(i*i for i in range(100))

if __name__ == '__main__':
    print(Widget.__dict__)
    print(Widget.complex_attr_may_not_need)
    print(Widget.__dict__)
    print(Widget.__dict__.get('complex_attr_may_not_need'))

# 类装饰器，会把属性复制到类obj的__dict__中去
# class A(object):
# 	def __init__(self, func):
# 		print('1: ', self.__dict__)
# 		import functools
# 		functools.update_wrapper(self, func)
# 		print('2: ', self.__dict__)
#
# 	def __get__(self, *args, **kwargs):
# 		print('get...', self.__dict__, args, kwargs, sep='\n')
#
# 	def __call__(self, *args, **kwargs):
# 		print('call...', self.__dict__, args, kwargs, sep='\n')
#
#
# @A
# def b():
# 	print('b...')
#
# # print(b)
# a = A(b)
# print(a.__name__)
# b()