#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import TypeVar, Generic

MyType = TypeVar("MyType", int, str)

class MyList(object, Generic[MyType]):

    def __init__(self, val: list):
        self.list: list = val

    def __getitem__(self, item) -> MyType:
        return self.list[item]


a = MyList([1])
b = a[0] # 调用__getitem__方法
print(b)

