# 装饰器 不影响原有函数功能，添加新的功能 语法 @
def func1(func):  # 外部函数接收被装饰函数的对象
    def func2():
        print("a1")
        return func()  # 闭包函数返回被装饰函数的调用
    return func2


@func1  # 把被装饰函数my_print传入func1
def my_print():
    print("hello world!")


my_print()  # func1(my_print)()


# 带参数的装饰器
# 1.被装饰的函数带参数，只需在闭包函数内传入参数即可
def func1(func):
    def func2(x, y):  # 闭包函数接收被装饰函数的参数，并做修改
        print(x, y)
        x += 5
        y += 5
        return func(x, y)  # 返回 被装饰函数的调用（修改了参数）
    return func2


@func1
def sum1(a, b):
    print(a + b)


sum1(1, 2)
