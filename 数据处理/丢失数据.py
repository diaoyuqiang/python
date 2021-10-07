import numpy
import pandas as pd  # 表格数据结构：series 与 dataframe
import numpy as np


# 日期索引列表
d = pd.date_range('20210809', periods=5)
# print(d)

# 生成五行四列的矩阵，行索引为d，列名为a,b,c,d
df = pd.DataFrame(np.arange(0, 20).reshape((5, 4)), index=d, columns=['a', 'b', 'c', 'd'])
print(df)

df.iloc[1, 1] = np.nan  # 设置空值
df.iloc[2, 1] = np.nan

print(df.dropna(axis=0, how='any'))  # 横向查找删除存在空值的行，how=all: 都为空才会删除

print(df.fillna(value=1))  # 给空值赋值

print(np.any(df.isnull()))  # 查看矩阵是否存在空值