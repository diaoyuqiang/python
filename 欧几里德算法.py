# 辗转相除法(求两个整数的最大公约数) 两个整数的最大公约数：较小的那个数和两数相除的余数的最大公约数
# def gcd(a, b):
#     if a < b:
#         a, b = b, a
#
#     num = a % b
#     while num != 0:
#         a, b = b, num
#         num = a % b
#
#     else:
#         return b
#
#
# c = gcd(4, 4)
# print(c)


# 递归方法
def gcd(a, b):
    if a < b:
        a, b = b, a
    return a if b == 0 else gcd(b, a % b)  # [值1 if 条件表达式 else 值2]：条件真返回左边的值，假返回右边的值


if __name__ == "__main__":
    print(gcd(5, 2))



