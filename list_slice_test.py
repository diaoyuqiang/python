#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 创建一个数字列表，代表我有100页文章，然后进行分页显示
mage = list(range(1, 101))
max_count = len(mage)  # 使用len()获取列表的长度，上节学的

n = 0
while n < max_count:  # 这里用到了一个while循环，穿越过来的
    print(mage[n:n + 10])  # 列表切片操作允许超出索引范围
    n = n + 10
