#!/usr/bin/env python
# -*- coding: utf-8 -*-
class C: pass

obj = C()
def func(): pass

print(sorted(set(dir(func)) - set(dir(obj))))  # 函数对象和实例对象的属性差别
