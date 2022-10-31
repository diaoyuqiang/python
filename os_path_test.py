#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

curr_path = '.'
file_name = 'os_path_test.py'

# print(os.getcwd())  # 返回当前工作路径
print(os.listdir(os.getcwd()))  # 返回当前路径的下的文件及文件夹列表

# os.remove(path) # 删除文件
# os.removedirs() # 方法用于递归删除目录
# fd = os.open()  # 打开文件,并返回文件描述符
# os.chdir(fd)  # 将当前工作目录切换到指定路径
# os.fchdir(path)  # 根据文件符修改当前目录

# fct = os.path.getctime('os_path_test.py')  # 获取文件的创建时间
# print(fct)
# print(time.ctime(fct))  # 将ctime转化为标准格式