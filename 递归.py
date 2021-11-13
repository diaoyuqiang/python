# 递归 1.调用自身  2.结束条件
def func1(x):  # 先递归再打印
    if x > 0:
        func1(x - 1)
        print(x)


func1(4)
