# a、调用的时机不同，__str__是在生成对象
# b、列表以及字典等容器总是会使用 __repr__ 方法。即使你显式的调用 str 方法，也是如此。
# c、我们需要显示的指定以何种方式进行类到字符串的转化，我们可以使用内置的 str() 或 repr() 方法，它们会调用类中对应的双下划线方法。
# d、__str__ 的返回结果可读性强，得到便于人们阅读的信息。__repr__ 的返回结果应更准确，__repr__ 存在的目的在于调试，便于开发者使用。将 __repr__ 返回的方式直接复制到命令行上，是可以直接执行的。
# e、自己写class的时候要加__repr__,如果没有添加 __str__ 方法，Python 在需要该方法但找不到的时候，它会去调用 __repr__ 方法。因此，在写自己的类的时候至少添加一个 __repr__ 方法，这能保证类到字符串始终有一个有效的自定义转换方式。
# f、在同一个类中，同时有__str__,__repr__,默认调用的是__str__。
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s的年龄是：%d" % (self.name, self.age)

    def __repr__(self):
        return "__repr__:{0}:{1}".format(self.name,self.age)

zs = Student("张三", 20)
ls = Student("李四", 18)
print(zs)
print(ls)
print("str调用：" + str(zs))
print("repr调用：" + repr(zs))
print("容器：" + str([ls]))
