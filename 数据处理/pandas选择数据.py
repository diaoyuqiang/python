import pandas as pd  # 表格数据结构：series 与 dataframe
import numpy as np

# 日期索引列表
d = pd.date_range('20210809', periods=5)
# print(d)

# 生成五行四列的矩阵，行索引为d，列名为a,b,c,d
df = pd.DataFrame(np.arange(0, 20).reshape((5, 4)), index=d, columns=['a', 'b', 'c', 'd'])
print(df)
print(df.a)  # 打印列表第一列
print(df[0:3])  # 打印0-3行

# 通过标签页选择
print(df.loc['20210809'])  # 打印20210809标签的数据
print(df.loc[:, ['a', 'c']])  # 打印a、c两列所有的行数据
print(df.loc['20210809', ['a', 'c']])  # 行：20210809 列：a、c

# 通过列表位置选择
print(df.iloc[1])  # 第二行(1为索引位置)
print(df.iloc[1, 1])  # 第二行的第二个value
# print(df.iloc[1:3, 1:3])  # 第二行到第三行，第二列到第三列 的数据
print(df.iloc[[1, 3], 1:3])  # 在第二列到第三列中选择 2-3行的数据

