#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 数据转圜
def convert(data):
    if isinstance(data, bytes):  return data.decode()
    if isinstance(data, dict):   return dict(map(convert, data.items()))
    if isinstance(data, tuple):  return map(convert, data)
    return data



dic = {"a":1, "b":2}
print(convert(dic))
# print(type(dic.items()))