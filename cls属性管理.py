# 类属性管理
class Employee:
    "所有员工的基类"
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name)


# __doc__: 类文档字符串
print(Employee.__doc__)
# __name__: 类名
print(Employee.__name__)
# __module__: 类所在模块
print(Employee.__module__)
# __bases__: 类的父类元组
print(Employee.__bases__)
# __dict__ : 类的属性(字典)
print(Employee.__dict__)