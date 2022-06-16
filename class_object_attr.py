class People(object):
    addr = "shanghai"

p = People()
# 实例对象修改类属性，只对本实例有用
p.addr = "shandong"
print(p.addr)
print(People.addr)
del p.addr
# 实例本身的类属性删除后，调用的是原先类属性的值
print(p.addr)