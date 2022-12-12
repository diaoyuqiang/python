#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Mymeta(type):  # 只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    n = 444

    def __new__(cls, *args, **kwargs):
        # print(args)  # 相当于name, object, attrs(dict)
        class_ = type.__new__(cls, *args, **kwargs)  # 必须按照这种传值方式, 此时的obj为OldboyTeacher
        # print(class_.__dict__)
        # return obj # 只有在返回值是type的对象时，才会触发下面的__init__
        print(class_)
        return class_

    # def __init__(self, class_name, class_bases, class_dic):
    #     print('run。。。')


class OldboyTeacher(object, metaclass=Mymeta):  # OldboyTeacher=Mymeta('OldboyTeacher',(object),{...})
    n = 111

    school = 'oldboy'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('%s says welcome to the oldboy to learn Python' % self.name)


# print(type(Mymeta))  # <class 'type'>
old = OldboyTeacher("a", 1)
print(old.__dict__)