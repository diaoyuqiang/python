import csv
from operator import sub
from random import choices
from datetime import date, timedelta
import pandas as pd

foods_category = {'蛋白质':('牛排', '火腿', '鸡肉', '鱼'), '碳水化合物': ('面包', '米饭', '苹果', '马铃薯', '芒果')}
# 每种食物所属类别
foods_category_reversed = {f: k for k,v in foods_category.items() for f in v}
# 用sum合并元祖
foods = sum(foods_category.values(), ())


file_path = 'data_foods.csv'
# 100天一日三餐的食物写进csv文件
with open(file_path, 'w', encoding='utf8', newline='') as f:
    w = csv.writer(f)
    w.writerow(('日期', '一日三餐'))  # 列头为元祖数据
    start = date(2022, 1, 1)
    for _ in range(100):
        w.writerow((str(start), ''.join(choices(foods, k=3))))  # 指定k后返回的是选取元素的列表
        start = start + timedelta(days=1)

# 读取数据
df = pd.read_csv(file_path, encoding='utf8')
# df['一日三餐'] = df['一日三餐'].str.split()  # 将pandas对象的一日三餐列分割成列表形式
df = df.explode('一日三餐', ignore_index=True).drop('日期', axis=1)  # explode: 将列表形式的pd对象转化为行， 去掉日期列
print(df)