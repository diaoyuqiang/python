#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 例子
class A:
    def test(self):
        print('A.test()')
        super().test()  # 调用A的test后,super调用其第二个父类的test方法


class B:
    def test(self):
        print('from B')


class C(A, B):
    pass


obj = C()

print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
obj.test()
