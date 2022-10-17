#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast

name = '露琪亚'
print([b for b in name.encode('utf-8')])  # 字节数组， 一个汉字三个字节(uint8)
a = ast.literal_eval('(20)')
print(a)
# print(type(a))

def run(params):
    a, b = params
    print(a, b)

run((1, 2))

orders = ['affff', 'bbbbfffff']
print([v for i, v in enumerate('abc')])