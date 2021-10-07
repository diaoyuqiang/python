# 闭包

def func():  # 外部函数
    a = 1   # 外部函数作用域里的变量
    print("this is func")

    def func1(num):  # 内部函数 闭包函数私有化了外部变量，完成了数据的封装，类似于面向对象
        print("this is func1")
        print(num + a)
    return func1  # 返回闭包函数

# 调用外部函数func，内部的func1就被创建了

# func()(3)


obj = func()   # 变量obj接收return返回的内部函数func1，所以obj即为func1
# 调用obj，利用内部函数访问外部函数作用域里的变量
obj(3)

list1 = [1, 2, 3, 4]


def func2(obj1):
    print("func2", obj1)

    def func3():
        obj1[0] += 1
        print("func3", obj1)
    return func3


var = func2(list1)  # var 内部函数对象
# del var # 删除内部函数对象（清除var所占的内存）
var()
# func2(list)()

