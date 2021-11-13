# 位置参数的顺序固定，不可变 arg,*args,*kwargs
# *args:将位置参数打包成元祖类型
# *kwargs:将关键字参数打包成字典类型

def function(arg, *args, **kwargs):
    print(arg, args, kwargs)


function(6, 7, 8, 9, a=1, b=2, c=3)