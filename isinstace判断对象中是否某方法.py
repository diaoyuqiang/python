import abc


class A(metaclass=abc.ABCMeta):  # metaclass: 可以动态的定制或修改继承它的子类  | 元类: ABCMeta
    @classmethod
    # __subclasshook__定义在抽象基类中
    # __subclasshook__，同时作用于isinstance和issubclass。而__instancecheck__只作用于isinstance函数，__subclasscheck__只作用于issubclass函数。
    def __subclasshook__(cls, subclass):
        # 存在greet()返回True，不存在返回False
        if hasattr(subclass, "greet"):
            return True
        return False


class B(object):
    def greet(self):  # 定义了greet()方法
        pass


class C(object):  # 没有greet()方法
    pass


class D(B):  # 继承自B类，因此继承了greet()方法
    pass


if __name__ == "__main__":
    b = B()
    c = C()
    d = D()

    # isinstance考虑继承
    print(isinstance(b, A))  # True
    print(isinstance(c, A))  # False
    print(isinstance(d, A))  # True
    # setattr(D, 'age', 18)
    # print(type(C)) <class 'type'>
