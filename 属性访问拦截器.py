#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):

    country = "china"  #类属性不会放到__dict__中
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        """
        base_info['robot_state'] 支持此方式取值
        :param item:
        :return:
        """
        return self.__dict__[item]


    def get(self, key):
        """
        支持  base_info.get('key') 方式取值
        :param key:
        :return:
        """
        return self.__dict__[key]

    # 实例属性访问拦截器
    def __getattribute__(self, attr): #注意：attr是传入的属性名,不是属性值
        print("开始属性校验拦截功能")
        print(attr)
        if attr == "name":  #注意这里引用原属性名不用self，直接引号引起来即可。
            print("现在开始调用的是name属性")
        elif attr =="age":
            print("现在开始调用的是age属性")
        else:
            print("现在调用的是其他属性")
            # print(type(super(Student, self).__getattribute__(attr)))
            func_ = super(Student, self).__getattribute__(attr)
            if type(func_) == "<class 'method'>":
                return func_
        # return object.__getattribute__(self, attr) #返回属性
        return super(Student, self).__getattribute__(attr)  # 继承object的类,默认存在属性拦截器, object为直接返回


s1 = Student("tom",19)
print(s1.get("age"))

