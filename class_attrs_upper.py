#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Mymetaclass(type):
    def __new__(cls, name, base, attrs):  # 元类中的__new__, __init__ == cls, name, base, attrs
        upper_attrs = {}
        # print(name)
        for k,v in attrs.items():  # 将类属性转换成大写
            if not callable(v) and not k.startswith("__"):
                upper_attrs[k.upper()] = v
            else:
                upper_attrs[k] = v
        return type.__new__(cls, name, base, upper_attrs)


class Chinese(metaclass=Mymetaclass):

    country='China'
    tag='Legend of the Dragon' #龙的传人


print(Chinese.__dict__)