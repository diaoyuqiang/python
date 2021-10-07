import sys

# num = 10
# _str = '小明'
#
# print(type(num), type(_str))
# print(id(num))
#
# num = '测试'
# print(id(num), num)
#
# print(isinstance(_str, (str,)))
#
# print(9 // 2)  # 取整除
# print(5 % 2)  # 取模


class Free(object):
    bar = 1


obj = Free()

# python自省
print(dir(obj))  # 获取对象的内部属性
print(type(obj))  # 获取对象类型
print(isinstance(obj, Free))  # 判断对象是否为个类型
print(getattr(obj, 'bar1', '没有'))  # 获取对象的属性
print(hasattr(obj, 'bar'))  # 判断对象中是否包含某属性

# del obj  # 删除对象的引用，对象由GC垃圾自动回收机制删除
print(sys.getrefcount(obj))  # 查看对象被引用的次数
