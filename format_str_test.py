print("{0:3d},{1:4s},{1:5s},{2}".format(11,"a",33)) # ' 11,a   ,a    ,33'  {0:3d}: 指定宽度

#通过下标也行
a=[1,2]
print('{0[0]},{0[1]}'.format(a))          #1,2

#对象属性
class Test(object):
    def __init__(self,name,age):
        self.name,self.age = name,age

    def __str__(self):
        return 'This boy is {self.name},is {self.age} old'.format(self=self)

    def str(self):
        return self.__str__()
a = Test('lilei',12)
print(str(a))    #This boy is lilei,is 12 old
print(a.str())   #This boy is lilei,is 12 old

#format函数单独使用
format('abc',"10s")     #'abc