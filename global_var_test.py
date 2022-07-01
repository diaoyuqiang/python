global_var = 0         #全局作用域
print(global_var, id(global_var))
def outer():
    enclosing_var = 1    #闭包函数外的函数中
    print(enclosing_var, id(enclosing_var))
    def inner():
        # enclosing_var = 2
        print(enclosing_var, id(enclosing_var))  # 闭包函数使用外部函数作用域里的变量
    inner()

outer()

import builtins  # 内置模块
# 查看预定义变量
print(dir(builtins))