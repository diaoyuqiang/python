class Tree():
    a = 1
    def __init__(self):
        self.x = "xx"



t = Tree()
print(Tree.__module__)  # 表示当前操作的对象在哪个模块
print(Tree.__dict__)
print(t.__dict__)