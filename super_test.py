class Base:
   def __init__(self, value):
       self.value = value


# class One(Base):
#    def __init__(self, value):
#        super(One,self).__init__(value)# super(本身类名,self).方法名(参数)这样就可以调用父类的方法和参数了
#        self.value *= 2

class One(Base):
   def __init__(self, value):
       super(One,self).__init__(value * 2)# super(本身类名,self).方法名(参数)这样就可以调用父类的方法和参数了


# class Two(Base):
#    def __init__(self, value):
#        super(Two,self).__init__(value)
#        self.value += 3

class Two(Base):
   def __init__(self, value):
       super(Two,self).__init__(value + 3)


class Ways(One, Two):  # 子类继承向上查找的顺序为继承顺序; 执行子类实现方法的时候，相当于函数的压栈，为继承的逆序.one先进，two先执行
   # super是继承父代
   def __init__(self, value):
       super(Ways,self).__init__(value)

foo = Ways(5)
print(foo.value) # 菱形继承问题

