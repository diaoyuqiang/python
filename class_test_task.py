#!/usr/bin/env python
# -*- coding: utf-8 -*-
class People:
    __country = 'China'  # _People__country='China'
    __n = 111  # _People__n=111

    def __init__(self, name):
        self.__name = name  # self._People__name=name
        self.a = 1

    def run(self):
        print('%s is running' % self.__name)  # self._People__name


# print(People.__country)#访问不到会报错

obj = People('egon')
# print(obj.__name)#访问不到会报错
obj.run()

print(People.__dict__)
print(People._People__country)  # 这样就能访问到
print(obj.__dict__)
print(obj._People__name)  # 这样就能访问到


# 总结这种隐藏需要注意的问题:
# 1. 这种隐藏只是一种语法上的变形,并没有真的限制访问
# 2. 这种变形只在类定义阶段检测语法时变形一次,类定义阶段之后新增的__开头的属性不会发生变形
# 3. 在继承中，父类如果不想让子类覆盖自己的方法，可以在该方法前加__开头

class Foo:
    def __f1(self):  # _Foo__f1
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.__f1()  # self._Foo__f1()


class Bar(Foo):
    def __f1(self):  # _Bar__f1
        print('Bar.f1')


obj = Bar()
obj.f2()