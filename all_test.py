#!/usr/bin/env python
# -*- coding: utf-8 -*-
lis = [{}, {"a": 10}]
lis1 = ['1', '2', ""]
lis2 = []
lis3 = [0, 9]
# all(iterable): 判断给定的可迭代iterable对象中的所有元素是否都为 TRUE
# 列表list, 元素都不为空或0才是true
print(all(lis))
print(all(lis1))
print(all(lis2))
print(all(lis3))
