import pickle  # 序列化模块
import json
import msgpack  # 序列化模块，比json速度快，长度小

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
# json.dumps 序列化时对中文默认使用的ascii编码
print(json.dumps(p))  # print(json.dumps(p, ensure_ascii=False)): 输出中文

jms = json.dumps(p)
# json格式反序列化
print(json.loads(jms))


var = {'a': 'this',
       'b': 'is',
       'c': 'a test'
}

with open('data.txt', 'wb') as f1:
    msgpack.dump(var, f1)  # 序列化存储数据

with open('data.txt', 'rb') as f2:
    var = msgpack.load(f2, use_list=True)  # 反序列化读取数据
print(var)
