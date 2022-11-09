#!/usr/bin/env python
# -*- coding: utf-8 -*-
class C(object):
    """
   存在了__get__的方法的类称之为描述符类
    descriptor 的实例自己访问自己是不会触发__get__，而会触发__call__，只有 descriptor 作为其它类的属性的时候才会触发 __get___
    """
    a = 'abc'

    def __get__(self, instance, owner):
        """

        @param instance: 被描述符的实例C2的实例
        @param owner: 被秒速的类名C2
        @return:
        """
        print("__get__() is called", instance, owner)
        print(self) # self 传的是C 本身的实例
        g = instance.m #看看这里调用的是C2的类属性m, 赋值给g
        print(g)

        return self

    def bb(self):
        print("调用了 get")

class C2(object):
    # 为了使用一个描述器，需将这个描述器的实例作为类属性放到一个类的定义中.
    d = C()
    m=1

    def ren(self):
        self.d.bb() # self.d 会先去执行C类的__get__里面的代码返回C类的self self去调用C类里面的bb()，而并不是调用了C2自己的bb

    def bb(self):
        print("调用了CS的bb函数")

if __name__ == '__main__':
    # 当调用d 会自动去调用描述类C中的__get__
    C2().ren()


