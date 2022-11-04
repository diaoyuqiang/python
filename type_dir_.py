#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
type(object)->对象的类型
type(name, bases, dict)->新类
"""

print(type('a'))
# type生成新类: 类名、基类元祖、类内定义的命名空间
X = type('x', (object, ), dict(a=1))
print(X().a)
