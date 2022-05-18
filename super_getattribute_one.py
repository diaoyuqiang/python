#coding=utf8
class Btt(object):
    pass
    def __init__(self):
        self.m = 1


class Aer(object):
    c = Btt
    def __init__(self):
        self.a = 'aa'

    def __getattribute__(self, item):
        # super(type, object) 返回-> super object: 解决单继承问题
        da = super(Aer, self).__getattribute__(item)
        # da = super().__getattribute__(item)
        # 重写getattribute,如果是类的方法直接返回，其他属性禁止访问
        if str(type(da)) == "<class 'method'>":
            return da
        else:
            return 'forbid visit attribute'
        # return da

    def run(self):
        print('start')

a = Aer()
print(a.a, type(a.run))
# print(Aer.__dict__)

# super 继承查找顺序
class A:
    def funxx(self):
        print("找到 funxx() 位于 A 中...")

class B(A):
    pass

class C(A):
    def funxx(self):
        print("找到 funxx() 位于 C 中...")

class D(A):
    def funxx(self):
        print("找到 funxx() 位于 D 中...")

class E(B, C):
    pass

class F(E, D):
    def funff(self):
        print("执行 F 中的 funff()...")
        super().funxx()


# print(f"F 类的 MRO : {F.__mro__}")
f = F()
f.funff()  # 查找顺序 F->E->B_>C->D->A->object