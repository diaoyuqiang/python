#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Father(object):
    def father_a(self):
        return self.b  # 这里为子类的self


class Son(Father):
    b = 10


if __name__ == '__main__':
    s = Son()
    print(s.father_a())  # 父类中调用子类的属性
