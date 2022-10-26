#!/usr/bin/env python
# -*- coding: utf-8 -*-

# def sum1(*args):
#     def sum2():
#         x = 0
#         for i in args:
#             x += i
#         return x
#     # 返回闭包函数
#     return sum2
#
#
# a = sum1(1, 2, 3)
# print(a())

# 返回函数列表
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
print(count())

# def chunks(get, n):
#     return [get[i:i + n] for i in range(0, len(get), n)]
#
# print(chunks([0,1,2,3,4,5,6], 2))
#
# a = [0,1,2,3,4,5,6]
# print(a[6:15])  # 列表切片操作允许超出索引范围



