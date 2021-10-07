import pandas as pd  # 表格数据结构：series 与 dataframe
import numpy as np

s = pd.Series([1, 2, 3, 4, np.nan, 9])
print(s)

# 日期索引列表
d = pd.date_range('20210809', periods=5)
print(d)

# 生成五行四列的矩阵，行索引为d，列名为a,b,c,d
df = pd.DataFrame(np.random.randn(5, 4), index=d, columns=['a', 'b', 'c', 'd'])
print(df)

print(df.values)  # 打印列表值
print(df.T)  # 行列转换
print(df.sort_index(axis=1, ascending=False))  # 对行索引倒序排序
print(df.sort_values(by='a'))  # 对列表值排序