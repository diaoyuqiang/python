#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce

# reduce() 函数会对参数序列中元素进行累积
sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
print(sum2)