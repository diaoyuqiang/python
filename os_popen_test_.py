#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# a = os.system("dir")  # 执行命令返回退出状态码
# print("a:", a)

b = os.popen("type text")  # 通过管道实现, 返回文件对象, read, readlines读取命令执行结果
# ret = b.read().strip().split('\n')
print(b.read())
b.close()