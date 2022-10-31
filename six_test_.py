#!/usr/bin/env python
# -*- coding: utf-8 -*-
import six  # SIX是用于python2与python3兼容的库

dic = {'name': 'dyq', 'age': 18}
ret = six.iteritems(dic)  # 返回字典项目的迭代器
print(ret)

for k, v in ret:
    print(k, v)

from six import get_unbound_function

class X(object):
    def method(self):
        pass

un_func = get_unbound_function(X.method(X))