# class 定义的类都为type类的实例对象
# python中一切都是对象，类也是对象；只不过是一种特殊的对象，是type的对象，type是python中的元类
def hello(self):
    self.name = 10
    print("hello world")


# type函数动态创建类
t = type("hello", (), {"a": 1, "hello": hello})
# print(type(t))  # type
T = t()  # type类实例赋值给T，T为class类

print(T.a)
T.hello()
print(T.name)


