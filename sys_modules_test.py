#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sys.modules包含了所有加载的模块。import语句在实际从磁盘上加载模块之前, 会先去检查这个字典！
import sys

# m = sys.modules  # 导入模块的全局字典
print(sys.modules['os'].__file__)  # os模块的路径
print(sys.modules[__name__].__name__)  # 当前模块的名称
# print(sys.modules.values())
# print(sys.modules.keys())

dic = {}
import json
dic1 = json.dumps(dic)
print(json.loads(dic1))