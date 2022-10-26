#!/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing  # 内置多进程包

print(multiprocessing.cpu_count())  # 获取cpu的逻辑内核数