import pickle  # 序列化模块
import json

p = {"name": "小明", "age": "18"}

# 序列化: 将p转换成二进制数据
bms = pickle.dumps(p)
# print(bms)

# 反序列化
print(pickle.loads(bms))

# 序列化写入文件
data = {"name": "小红", "age": "20"}
with open('pick.txt', 'wb') as f:
    pickle.dump(data, f)

# 反序列化读取二进制文件
with open('pick.txt','rb') as e:
    p = pickle.load(e)
print(p)

# json格式序列化
p = {"first": "tom", "last": "杰克"}
print(json.dumps(p))

jms = json.dumps(p)
# json格式反序列化
print(json.loads(jms))

