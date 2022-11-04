#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python2

import sys

default_en = sys.getdefaultencoding()
print default_en  # py2中默认ascii编码

reload(sys)  # 重新载入系统模块
sys.setdefaultencoding('utf-8')  # 设置默认编码方式

curr_en = sys.getdefaultencoding()
print curr_en
