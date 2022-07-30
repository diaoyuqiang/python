import random
a = [10,2,3]
# 累加权重取第一位
print(random.choices(a,cum_weights=[1,1,1],k=6))  # k返回的列表长度