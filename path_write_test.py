#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import pathlib

path = '.'
if getattr(sys, 'frozen', False):  # 程序打包后会添加frozen属性
    # 获取可执行程序的目录
    path = os.path.dirname(sys.executable)
elif __file__:
    path = os.path.dirname(__file__)

# print(path)

with open(pathlib.Path(path, 'ui.json').absolute(), 'w+') as f:
    f.write('{"a": "b"}')