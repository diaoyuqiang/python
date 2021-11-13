"""
uuid1():
从主机ID、序列号和当前时间生成UUID

uuid4():
生成一个随机UUID。
"""

import uuid

a = uuid.uuid1()
print(a)