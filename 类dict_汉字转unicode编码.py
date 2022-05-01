class Tree:
    a = 1
    def __init__(self):
        self.b = "str"

    def run(self):
        return self.b


t = Tree()
print(isinstance(Tree, type))
print(Tree.__dict__.items())  # 类属性、方法等的items

# 汉字转Unicode编码
sr = "与"
da = ""
for x in sr:
    da += r"\u" + hex(ord(x))[2:]
print(f"unicode编码为:{da}")
print('\u4e0e')