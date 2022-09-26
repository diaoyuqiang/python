#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

# PyInstaller打包后的程序会有'frozen'属性, 表示代码可以在当前环境运行
if getattr(sys, 'frozen', False):
    # sys.executable: python解释器的路径
    path = os.path.dirname(sys.executable)
    # print('path:', path)
elif __file__:
    # 当前文件的目录
    path = os.path.dirname(__file__)
    print(path)