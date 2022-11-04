#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 类属性和实例属性的访问
# 类属性属于类，实例属性属于对象
# 类属性在内存中只保存一份，实例属性在每个对象中都保留一份
# 对于类属性，类可以访问到，实例对象也可以访问到；对于实例属性，类访问不到，实例对象可以访问到
class Build(object):
    frame = []

    def __init__(self):
        self.frame1 = [1, 2]

b = Build()

print(Build.frame)
print(b.frame)
