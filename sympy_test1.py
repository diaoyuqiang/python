#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *  # 数学库

# 常用函数及变量
print(cos(pi))

# 定义多个变量
x1, y, z = symbols('x1 y z')

# 定义分数
r = Rational(1, 2)
print(r)

# 定义x的正整数
x = symbols('x', Integer=True, positive=True)

# 多项式展开
print(expand((x + 1) **2))

# 因式分解
print(factor(x**2 + 2*x + 1))

# 定义数学中的函数
expr = cos(x) + r
# 表达式传入变量值
ret = expr.subs(x, 0)
print(ret)

# 简化表达式
h = symbols('n')
expr1 = sin(h) **2 + cos(h) **2
simp = sympify(expr1)
print(simp)
