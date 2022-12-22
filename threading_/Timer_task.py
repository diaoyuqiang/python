#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import threading
import time


def func1(a):
    # Do something
    print('Do something')
    a += 1
    print(a)  # 函数递归次数
    print('当前活跃线程数为:{}, 线程nm:{}'.format(threading.activeCount() , threading.currentThread().name))
    if a > 4:
        return

    t = threading.Timer(5, func1, (a,))  # 每次启动一个新的线程去递归，直到触发递归结束条件
    t.start()


func1(0)
# print(str("" or "dyq"))