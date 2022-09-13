#!/usr/bin/env python
# -*- coding: utf-8 -*-
from atexit import register  # 注册解释器退出前的回调函数，先进后出

def reg_1():
    print('I`m reg1 ')

def reg_2(name):
    print('I`m reg2 %s'%(name))


register(reg_1)
register(reg_2,'reg2')

@register
def reg_4():
    print('I`m reg4')
