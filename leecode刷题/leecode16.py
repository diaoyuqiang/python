"""
一瓶酒 55 元，55 个酒瓶可以换 11 瓶酒，请问 n 元最多可以喝到几瓶酒？
"""

price = int(input("钱:"))


def beer(money):
    s = 0
    for i in range(1, money+1):
        if i % 5 == 0:
            s += 1
            if s % 5 == 0:
                s += 1
    return s


result = beer(price)
print(result)