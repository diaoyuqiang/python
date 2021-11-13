# 对象的属性管理

class Atree(object):
    def __init__(self):
        self.name = 'dyq'
        self.age = 18


a = Atree()
# getattr(obj, name[, default]) 获取对象属性
print(getattr(a, 'n1ame', 'None'))
# hasattr(obj, name) 判断对象是否有某属性
print(hasattr(a, 'name'))
# setattr(obj, name, value)  设置对象属性
setattr(a, 'cl', 10)
# print(getattr(a, 'cl', 'None'))
# delattr(obj, name)  删除对象中的属性
delattr(a, 'cl')