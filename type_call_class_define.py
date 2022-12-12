#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Mymeta(type):  # 只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    def __call__(cls, *args, **kwargs):  # cls=<class '__main__.OldboyTeacher'>
        # 1、调用__new__产生一个空对象obj
        obj = cls.__new__(cls, object, {})  # 此处的cls是类OldoyTeacher，必须传参，代表创建一个OldboyTeacher的对象obj
        # 2、调用__init__初始化空对象obj
        cls.__init__(obj, *args, **kwargs)
        # print(args)
        # print(kwargs)
        # 在初始化之后，obj.__dict__里就有值了
        obj.__dict__ = {'_%s__%s' % (cls.__name__, k): v for k, v in obj.__dict__.items()}
        # 3、返回初始化好的对象obj
        # print(self.__name__)  # 类米名称
        return obj


class OldboyTeacher(object, metaclass=Mymeta):
    school = 'oldboy'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('%s says welcome to the oldboy to learn Python' % self.name)


t1 = OldboyTeacher('egon', 18)
print(t1.__dict__)  # {'_OldboyTeacher__name': 'egon', '_OldboyTeacher__age': 18}
