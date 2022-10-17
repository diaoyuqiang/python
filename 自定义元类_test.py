#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Mymeta(type):  # 继承type生成自定义元类
    def __init__(self, class_name, class_bases, class_dict):  # 类名，基类，类dict
        super().__init__(class_name, class_bases, class_dict)
        print(self.__base__)  # 查看基类

        if not class_name.istitle():
            raise TypeError('类名%s首字母必须大写其余小写' % class_name)
        if '__doc__' not in class_dict or len(class_dict['__doc__'].strip(' \n')) == 0:
            raise TypeError('类中必须要有注释')


# 通过自定义元类创建class
class People(object, metaclass=Mymeta):  # 指定基类和元类
    """
    注释
    """
    def __init__(self):
        self.a = 1

