#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A(object):
    def __init__(self):
        print("class ---- A ----")


class B(A):
    def __init__(self):
        print("class ---- B ----")
        super(B, self).__init__()


class C(A):
    def __init__(self):
        print("class ---- C ----")
        super(C, self).__init__()


class D(B, C):
    def __init__(self):
        print(D.__mro__)  # 方法继承顺序
        print("class ---- D ----")
        super(D, self).__init__()


d = D()

