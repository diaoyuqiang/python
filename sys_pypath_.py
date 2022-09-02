#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
下面的两个方法可以将模块路径加到当前模块扫描的路径里：
sys.path.append('你的模块的名称')
sys.path.insert(0,'模块的名称')
永久添加路径到sys.path中，方式有三。

如下：
1）将写好的py文件放到已经添加到系统环境变量的目录下:
2) 在 /usr/lib/python2.6/site-packages 下面新建一个.pth 文件(以pth作为后缀名)；将模块的路径写进去，一行一个路径，如： vim pythonmodule.pth
/home/liu/shell/config
/home/liu/shell/base

3) 使用PYTHONPATH环境变量
export PYTHONPATH=$PYTHONPATH:/home/liu/shell/config
"""