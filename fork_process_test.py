#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import os

# 子进程从父进程继承了多个值的拷贝，比如全局变量和环境变量; 区别: 子进程返回0, 主进程返回子进程pid
pid = os.fork()  # fork创建子进程
if pid == 0:
    print("A", os.getpid(), os.getppid())
else:
    print("B", os.getpid(), os.getppid())
    # os.getpid()获取当前进程id; os.getppid()获取父进程id
