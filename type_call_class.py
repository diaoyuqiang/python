#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Mymeta(type):  # 只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    def __call__(cls, *args, **kwargs):
        print(cls)  # <class '__main__.OldboyTeacher'>
        print(args)  # ('egon', 18)
        print(kwargs)  # {}
        return 123


class OldboyTeacher(object, metaclass=Mymeta):
    school = 'oldboy'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        pass
        # print('%s says welcome to the oldboy to learn Python' % self.name)


# 调用OldboyTeacher就是在调用OldboyTeacher类中的__call__方法
# 然后将OldboyTeacher传给self,溢出的位置参数传给*，溢出的关键字参数传给**
# 调用OldboyTeacher的返回值就是调用__call__的返回值
t1 = OldboyTeacher('egon', 18)
print(t1)  # 123
