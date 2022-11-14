#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [start : end : step]

"""
 start:开始下标，从0开始

 end：结束下标,

 step：步长，步长为正时，从左向右取值。步长为负时，从右向左取值
 注意：步长不可以为0
"""
lis = [1, 2, 3, 4, 5, 6]

print(lis[1:3])  # : 截取操作
print(lis[-3:])  # 从索引位置-3开始截取(左->右)
print(lis[::-1])  # 倒序，从右向左截取
# print(lis[::-2])
print(lis[:3:-1])  # start省略，最后为-1代表从右向左截取到索引为3的元素(不包含3)
print(lis[2::-1])  # step为-1代表从右向左截取(end省略)