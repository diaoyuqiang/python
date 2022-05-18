import numpy as np
p = np.array([1, 2, 3])
print(np.sum(p, axis=0))
import scipy.special
print(scipy.special.comb(3, 0))  # 组合数即为伯恩斯坦多项式常数项系数
for t in np.linspace(0, 1, 5):  # 等差数列
    print(t)