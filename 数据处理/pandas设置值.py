import pandas as pd  # 表格数据结构：series 与 dataframe
import numpy as np

# 日期索引列表
d = pd.date_range('20210809', periods=5)
# print(d)

# 生成五行四列的矩阵，行索引为d，列名为a,b,c,d
df = pd.DataFrame(np.arange(0, 20).reshape((5, 4)), index=d, columns=['a', 'b', 'c', 'd'])
print(df)

# 索引位置设置列表值
df.iloc[2, 2] = 99  # 第二行第二列设置为99
# 标签设置列表值
df.loc['20210810', 'b'] = 88

df.a[df.a > 4] = 0  # a列大于4的设置为0
df['e'] = np.nan  # 添加e列，值为NaN
df['f'] = pd.Series([7, 8, 9, 10, 11], index=d)
print(df)

