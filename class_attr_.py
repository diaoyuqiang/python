#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Student:
    count=0
    def __init__(self,name):
        self.name=name
        Student.count+=1  # 类属性统计实例数量

obj1=Student('a')
obj2=Student('z')
print(Student.count)

l3 = []
list.append(l3, 1)  # 相当于l3.append()
print(l3)

dic = {}
d = {"1": 1}
# print(dic.update(d))
dic.update(d)
def run(d):
    print(d)

run(dic)