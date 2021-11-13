# 实例方法、类方法、静态方法、函数

"""
不想访问类变量和实例变量，可以用静态方法 @staticmethod ()
  只想访问类内变量，不想访问实例变量用类方法  @classmethod （cls, ）
  即想访问类变量，也想访问实例变量用实例方法  （self, ）
  函数与静态方法相同，只是静态方法的作用域定义在类内
"""


# 静态方法示例 类对象和实例对象都可访问静态方法，静态方法不能访问类变量和实例变量
class A:
    @staticmethod
    def add(a, b):
        return a + b


print(A.add(100, 200))
a = A()
print(a.add(3, 4))