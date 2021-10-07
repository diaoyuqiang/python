from enum import Enum, auto, unique  # auto() 自动赋值  @unique:确保唯一枚举值


# Gender枚举类
@unique
class Gender(Enum):
    male = 1
    female = 2
    un_know = 3


# 枚举成员
g = Gender.male
# t = Gender(1)
# f = Gender['female']

print(g)
print(g.name)  # 属性名
print(g.value)  # 属性值

# 迭代方式遍历枚举类属性
for i in Gender:
    print(i)


# # 定义枚举的第二种方法
# Gender_ = Enum('Gender_', [('male', '男'), ('female', '女性'), ('unk', '未知')])
#
# w = Gender_.unk
# e = Gender_('男')
# r = Gender_['female']
# print(w, e, r)