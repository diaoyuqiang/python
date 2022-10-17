"""
你的代码需要从标准输入流（控制台）中读入一个正整数 n，
然后计算区间 [1,n] 的所有素数，计算出结果并打印到标准输出流（控制台）中，每个素数占一行。
: 计算质数公式
"""
n = int(input('整数:'))
for i in range(2, n+1):  # 使用for循环遍历区间[2,n]
    isPrime = True
    for j in range(2, int(pow(i, 0.5)) + 1):  # 在 2 到 sqrt(i) 中判断有无 i 的因子
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)


# for i in range(2, 5):
#     print(i, type(i))  # i:int

# print(int(pow(5, 0.5)) + 1)
# print(int(1.87))