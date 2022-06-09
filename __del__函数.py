class Person(object):
    def __init__(self,name):
        self.name = name
    # 创建多个对象的时候触发__del__方法,释放对象，del关键字删除引用，使引用计数为0时，才会调用__del__方法
    def __del__(self):
        print("实例对象:%s"%self.name,id(self))
        print("python解释器开始回收%s对象了" % self.name)

print("类对象",id(Person))
zhangsan  = Person("张三")
print("实例对象张三:",id(zhangsan))
print("------------")
lisi  = Person("李四")
print("实例对象李四:",id(lisi))
