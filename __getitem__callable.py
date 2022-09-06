#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal:
    def __init__(self, animal_list):
        self.animals_name = animal_list
        self.other = 'hello, world'

    # 1.对象[‘key’]取值
    # 2.没有实现 __iter__ __next__, Python的解释器会去寻找__getitem__ 来迭代对象
    def __getitem__(self, index):
        return self.animals_name[index]

animals = Animal(["dog","cat","fish"])
for animal in animals:
    print(animal)

