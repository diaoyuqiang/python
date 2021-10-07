import random
import functools


# 装饰器函数
def decorator(func):
    @functools.wraps(func)  # wraps()装饰函数
    def pack():
        if random.randint(1, 10) <= 5:
            func()  # 真实函数的调用
        else:
            print("运气不佳。")
    return pack  # 返回闭包函数


# 真实函数
@decorator  # 语法糖（@装饰器函数）
def m_yun():
    print("你好，我是马云..")
# 调用装饰器
# dec = decorator(m_yun)
# dec()


m_yun()