import json
from google.protobuf.json_format import ParseDict
from protobuf_test.proto import hello_pb2
import struct

# protoc对象
req = hello_pb2.HelloRequest()
# ParseDict(dic, req)  将字典数据添加到protoc对象中


value = {"statisticsData": {"name": "dyq"}}
ParseDict(value, req)  # 将字典格式的数据解析到message中
# 序列化成字节字符串
da = req.SerializeToString()
# print(da, type(da))

# 字节字符串解析成str
req.ParseFromString(da)
# MessageToJson(req, including_default_value_fields=True)  # 将protobuf message数据序列化成json格式，空键值对也序列化
print(req.name) # 打印对象的值
