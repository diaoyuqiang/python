class A(object):
    def __init__(self, name):
        self.name = name

    # __getattr__只有在使用点调用属性且属性不存在的时候才会触发
    def __getattr__(self, attr):  # #当两个函数都存在时，只有__getattribute__抛出AttributeError才会执行
        return eval("self." + attr.lower())  # 对不存在的属性进行操作，eval后再次调用__getattribute__

    # 1. __getattribute__不管属性存不存在都会触发
    # 2. 只有在抛出AttributeError异常时，才会触发__getattr__函数
    def __getattribute__(self, item):
        return super().__getattribute__(item)


if __name__ == "__main__":
    a = A('小白')
    print("a.name -> {}".format(a.name))
    print("a.NAME -> {}".format(a.NAME))


# class Tag:
#     def __init__(self):
#         self.change = {'python': 'This is python',
#                        'php': 'PHP is a good language'}
#
#     def __getitem__(self, item):
#         print('调用getitem')
#         return self.change[item]
#
#     def __setitem__(self, key, value):
#         print('调用setitem')
#         self.change[key] = value
#
#
# a = Tag()
# print(a['php'])
# a['php'] = 'PHP is not a good language'
# print(a['php'])