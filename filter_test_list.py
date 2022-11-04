#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def test_for(length):
    sub_list = []
    begin = time.perf_counter()
    for i in range(length):
        if i % 2 == 0:
            sub_list.append(i)
    end = time.perf_counter()
    print('for循环耗时:', (end - begin))

# filter过滤器: 其作用是从列表（或其他序列类型）中筛选出满足条件的子列表
def test_filter(length):
    def check(i):
        return i % 2 == 0

    begin = time.perf_counter()  # 计时器: 返回秒为单位的浮点值
    sub_list = filter(check, range(length))
    end = time.perf_counter()
    print('filter耗时:', (end - begin))

test_for(100000)
test_filter(100000)
