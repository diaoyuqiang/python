from protobuf_test.proto import hello_pb2

# protoc对象
req = hello_pb2.HelloRequest()
# ParseDict(dic, req)  将字典数据添加到protoc对象中

req.name = "dyq"
# 序列化成字节字符串
nm = req.SerializeToString()
print(nm, type(nm))

# 字节字符串解析成
req.ParseFromString(nm)
# MessageToJson(req, including_default_value_fields=True)  # 将protobuf message数据序列化成json格式，空键值对也序列化
print(req.name) # 打印对象的值

import numpy as np

d = np.array([[1, 2],
             [2, 4]])
print(d)
print(d.dot(2))