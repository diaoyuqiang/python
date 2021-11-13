# 类继承: 先在本类中查找调用的方法，找不到才去基类中找
# issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)

class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        # 类属性
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)


class Child(Parent):  # 定义子类

    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法')


c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法

# 子类调用父类的方法
c.setAttr(200)  # 设置类属性值
c.getAttr()  # 获取类属性值


