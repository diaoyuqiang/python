#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python2.x中用 input() 相等于 eval(raw_input(prompt)), 字符串需要'', 一般用raw_input()

# py2 用input()输入字符串会报SyntaxError:
da = raw_input('input:')
print type(da)