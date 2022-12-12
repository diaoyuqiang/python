#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Mysql(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def tell_info(self):
        print(self.ip, self.port)

    @classmethod
    def connect(cls, ip, port):
        return cls(ip, port)  # 类方法返回创建的对象

m = Mysql.connect("127.0.0.1", "8080")
m.tell_info()