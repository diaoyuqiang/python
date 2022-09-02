#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
from pydantic import BaseModel  # 继承BaseModel, 建立一个符合所提供的类型和约束的模型


class Foo(BaseModel):
    count: int
    size: float = None  # 字段名: type = 默认值


class Bar(BaseModel):
    apple = 'x'
    banana = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]  # Bar模型实例列表


m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
print(m)
# print(m.json()) # json格式显示
print(m.__fields_set__)  # 模型中必填字段
#> foo=Foo(count=4, size=None) bars=[Bar(apple='x1', banana='y'),
#> Bar(apple='x2', banana='y')]
print(m.dict())
# """
# {
#     'foo': {'count': 4, 'size': None},
#     'bars': [
#         {'apple': 'x1', 'banana': 'y'},
#         {'apple': 'x2', 'banana': 'y'},
#     ],
# }
# """
