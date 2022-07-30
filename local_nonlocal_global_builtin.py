""""
最内层为local，外层为nonlocal，模块对应global。
变量查找的顺序：内层作用域 local （最内层函数）-> 外层 nonlocal（外层函数） -> 全局 global （模块）-> builtin （命名空间）
只有class、def和lamda会改变作用域。
"""

def scope_test():
    def do_local():
        spam = "local spam"  # 只是声明了一个新的局部变量，作用域：local

    def do_nonlocal():
        nonlocal spam   # 声明 nonlocal，即外层函数的变量
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam += " spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


spam = "global"   # 全局变量 global
scope_test()
print("In global scope:", spam)


