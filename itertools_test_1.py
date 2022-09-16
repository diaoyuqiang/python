#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

lis = [1,2,3]
a = itertools.islice(lis, None, None, 1)  # 返回序列seq的从start开始到stop结束的步长为step的元素的迭代器
# print(a)
for i in a:
    print(i)