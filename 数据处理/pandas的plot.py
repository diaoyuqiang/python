import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # 绘图库

df = pd.Series(np.random.randn(100), index=np.arange(100))  # 100个元素的一维数组
# print(df)
df = df.cumsum()  # 累加数组

df.plot()  # 数组绘制
# plt.show()  # 展示绘制的图形

# 4列100个元素的矩阵
data = pd.DataFrame(np.random.randn(100, 4), index=np.arange(100), columns=list('abcd'))
# print(data.head())  # 打印矩阵前5行

data = data.cumsum()
data.plot()
plt.show()

