#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Mymetaclass(type):
    def __call__(cls, *args, **kwargs):
        if args:
            raise TypeError('must use keyword argument for key function')
        obj = object.__new__(cls)
        # print(kwargs)
        for k, v in kwargs.items():
            obj.__dict__[k.upper()] = v
        return obj


class Chinese(metaclass=Mymetaclass):
    country = 'China'
    tag = 'Legend of the Dragon'  # 龙的传人

    def walk(self):
        print('%s is walking' % self.NAME)


p = Chinese(name='egon', age=18, sex='male')  # 使用元类生成对象的属性
print(p.__dict__)
p.walk()
