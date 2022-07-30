# python函数是一种对象，是对象就会有对象的属性。可以通过如下方式查看函数对象的属性：
def un():
    pass
un.var = 1

print(un.var)
print(dir(un))  # 查看对象属性