import pandas as pd

# 读取csv文件
data = pd.read_csv('student.csv')
print(data)

# 导出列表文件
data.to_pickle('student.pickle')