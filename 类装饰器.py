#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

# 类装饰器: init传入真实函数，call调用
class Decorator():
    def __init__(self, func):
        self.func = func

    def run(self):
        time.sleep(5)

    def __call__(self, *args, **kwargs):
        self.run()
        self.func()

# 带参数的类装饰器,参数由call接收
class Decorator_Params():
    def __init__(self, func):
        self.func = func

    def run(self, n):
        print(n)

    def __call__(self, *args, **kwargs):
        self.run(*args)
        self.func()

@Decorator_Params
def task():
    print("延时调用")

task(2)