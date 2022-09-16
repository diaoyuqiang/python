#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import functools

class shap():
    def __init__(self):
        self.a = 1
        self.dic = {"a": "a"}

    # 类中的装饰器
    def execute_time_interval(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            t_i = func.__name__ + "_time_interval"
            if not getattr(self, t_i, None):
                setattr(self, t_i, time.time())
                return func(self, *args, **kwargs)
            else:
                if time.time() - getattr(self, t_i) > 0.15:
                    setattr(self, t_i, time.time())
                    return func(self, *args, **kwargs)
        return wrapper

    @execute_time_interval
    def run(self, a):
        return getattr(self, a)  # 获取对象的属性

    def put(self):
        setattr(self, 'b', "b")  # 设置对象属性

    def get(self):
        return self.__dict__  # 对象的属性字典

sh = shap()
print(sh.run("a"))
# time.sleep(1)
print("None", sh.run("a"))
# sh.put()
# print(sh.b)
# print(sh.get())
#
# import json
# dic = {"是": 1}
# print(type(json.dumps(dic)))
# dic1 = '{"c": 2}'
# print(type(json.loads(dic1)))