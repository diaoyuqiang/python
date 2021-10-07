import numpy as np
import pandas as pd


df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])

# print(df1)
# print(df2)
# print(df3)

# 上下方向合并列表
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)  # ignore_index忽略原先的竖向索引
# print(res)


dw = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
dw1 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])

# 上下方向合并列表 取交集
res1 = pd.concat([dw, dw1], join='inner', axis=0, ignore_index=True)
# print(res1)

# 左右合并列表， dw1的索引更新为dw的索引
res2 = pd.concat([dw, dw1.reindex_like(dw)], axis=1)
# print(res2)

# 忽略原先的竖向索引，向df1中追加df2列表
skt = df1.append(df2, ignore_index=True)
print(skt)