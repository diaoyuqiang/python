#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 自定义字典类
class ObjectDict(dict):
    def __init__(self, *args, **kwargs):
        super(ObjectDict, self).__init__(*args, **kwargs)

    # 查询实例属性的最后一步
    def __getattr__(self, name):
        value =  self[name]
        if isinstance(value, dict):
            value = ObjectDict(value)
        return value

if __name__ == '__main__':
    od = ObjectDict(asf={'a': 1}, d=True)
    # print(od)
    print(od.asf, ';', type(od.asf))
    # print(od.asf.a)
    # print(od.d)