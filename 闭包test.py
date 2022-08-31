def outer():
    c = 3
    def inner(num):  # 闭包函数的参数可以私有化外部函数作用域里的变量，可以直接访问，但不能修改值
        a = num + c
        print(a)
    return inner

outer()(2)


# 修改外部嵌套函数变量使用nonlocal
def out1():
    c = 2
    def inner1():
        nonlocal c
        c += 1
        print(c)
    return inner1()

out1()