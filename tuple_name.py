from collections import namedtuple

# 定义命名元祖
Book = namedtuple("Book", "name price url")
a = Book("dyq", 10, "https://www.baidu.com")
# a = Book(name="dyq", price=10, url="https://www.baidu.com")
print(a)
print(a.name)

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age')

import csv
# 命名元祖读取csv文件，遍历数据字段
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "r"))):
    print(emp.name, emp.age)

import collections
# 将纸牌定义为具名元组，每个纸牌都有等级和花色
Card = collections.namedtuple('Card', 'rank suit')

# namedtuple纸牌
class FrenchDeck:
    # 等级2-A
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    # 花色红黑方草
    suits = 'spades diamonds clubs hearts'.split()
    # 构建纸牌
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    # 获取纸牌
    def __getitem__(self, position):
        return self._cards[position]

f = FrenchDeck()
a = f[1]
print(a)  # 命名元祖
print(a.rank)

# [列表生成器]
# a = [(a, b) for a in range(1,3) for b in range(4,6)]
# print(a)