import pandas as pd
import pickle

# 读取csv文件
data = pd.read_csv('student.csv')
# print(data)

# 导出序列化后的列表文件
data.to_pickle('student.pickle')
# 读取序列化后的文件
f = open('student.pickle', 'rb')
info = pickle.load(f)
print(info)