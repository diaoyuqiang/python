#!/usr/bin/env python
# -*- coding: utf-8 -*-
lst = ['1', '2', '3', '4', '5', '6']
lst_int = map(lambda x: int(x), lst)  # 根据提供的函数对指定序列做映射
print(list(lst_int))

lis1 = [1, 2, 3, 4]
lis2 = [4, 5, 6, 7]

def add(a, b):
    return a + b

print(list(map(add, lis1, lis2)))
