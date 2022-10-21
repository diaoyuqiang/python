#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

print(os.environ['HOMEPATH'])  # 用户的主目录
print(os.environ['PATHEXT'])  # 可执行文件
print(os.environ['LOGONSERVER'])  # 机器名称
print(os.environ['PROMPT'])  # 设置提示符

# flush: 强制刷新输出流
print("1", 1, "2 4", sep='', flush=True)  # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print("你是""谁")

# %-ns: 至少输出n个字符,不够右侧补空格
print("%-10s\t %-10s\t %-10s\t %-10s"%("学生号","姓名","科目","分数"))
print("%-15s\t %-11s\t %-10s\t %-12s"%("100000101","阿凡达","语文","80"))