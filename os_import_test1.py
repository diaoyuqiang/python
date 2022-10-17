#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast

# 读取文件
a = open(r'E:\time.txt', 'r').read()
print(a)

# __import__()函数 动态加载模块
__import__('os').system('dir')
# 弧度转角度
s = __import__('math').degrees(1.57079637)  # 90度
print(s)
# __import__('os').system('rm -rf /etc/*')
print(ast.literal_eval('1+1'))  # 安全的抽象语法解析工具