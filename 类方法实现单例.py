#!/usr/bin/env python
# -*- coding: utf-8 -*-
import settings


# 方法一: 类方法实现单例
class Mysql:
    __instance = None

    def __init__(self, host, port):
        self.host = host
        self.port = port

    @classmethod
    def assign(cls):
        if not cls.__instance:
            cls.__instance = cls(settings.HOST, settings.PORT)
        return cls.__instance


o = Mysql.assign()
o1 = Mysql.assign()


# obj1 = Mysql(settings.HOST, settings.PORT)
# obj2 = Mysql(settings.HOST, settings.PORT)
# print(id(obj1),  id(obj2))

# 方法二: 定制元类实现单例模式
class Mymeta(type):
    def __init__(cls, name, bases, dic):
        cls.__instance = object.__new__(cls)
        cls.__init__(cls.__instance, settings.HOST, settings.PORT)
        # 上述两步可以合成下面一步
        # cls.__instance = super().__call__(*args,**kwargs)
        super().__init__(name, bases, dic)

    def __call__(cls, *args, **kwargs):
        if args or kwargs:
            obj = object.__new__(cls)
            cls.__init__(obj, *args, **kwargs)
            return obj
        return cls.__instance


# class Mysql(metaclass=Mymeta):
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port

# obj1=Mysql() # 没有传值则默认从配置文件中读配置来实例化，所有的实例应该指向一个内存地址
# obj2=Mysql()

# 方法三: 定义一个装饰器实现单例模式
def singleton(cls):  # cls=Mysql
    _instance = cls(settings.HOST, settings.PORT)

    def wrapper(*args, **kwargs):
        if args or kwargs:
            obj = cls(*args, **kwargs)
            return obj
        return _instance

    return wrapper

# @singleton # Mysql=singleton(Mysql)
# class Mysql:
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port
#
# obj1=Mysql()
# obj2=Mysql()
# obj3=Mysql()
# print(obj1 is obj2 is obj3) #True
