import json
import os

def read(path):
    if os.path.exists(path):
        with open(path, 'r') as f:
           dict = json.load(f)  # 参数可以为文件对象
           print(dict)
    else:
        dic = {1:"a", 2:'b'}
        with open(path, 'w') as f:
            json.dump(dic, f)  # 序列化写入文件

read('4info.txt')

# 可以转化为python的基本数据类型
f = json.loads('22')
t = json.loads('["a", "b"]')
print(f, type(f))
print(t, type(t))