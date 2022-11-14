#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def hongbao(total, num):
    """
    |—|———————|—————————|——————————————|
    0                                  total
    :param total:
    :param num:
    :return:
    """
    if num * 0.01 > total:
        print('总金额过小！')
        return None
    else:
        result = []
        lst = random.sample(range(1, int(total * 100)), num - 1)  # 从序列中随机截取num-1个元素，返回新的序列
        lst.append(0)
        lst.append(total * 100)
        lst.sort()
        result = [(lst[i] - lst[i - 1]) / 100 for i in range(1, len(lst))]
        return result


print(hongbao(30, 5))
