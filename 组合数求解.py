from scipy.special import comb
import numpy as np

k = np.array([3, 4])
n = np.array([10, 10])
# 组合计算公式：C（n，m）=n!/m!（n-m）!1
# 求组合数
a = comb(n, k, exact=False)
print(a)
b = comb(10, 3, exact=True)  # 计算整数
print(b)