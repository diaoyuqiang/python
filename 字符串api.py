# 字符串api
# strip 去除字符串前后的空格
print("  life is not all rose  ".strip())
# count 返回子串出现的次数
print("life is not all rose".count("s", -15, -1))  # 索引位置[-15, -1]
# find  查找字符串出现的位置，不存在返回-1
print("life is not all rose".find("is"))
# index 查找字符串出现的位置，不存在报错
print("life is not all rose".index("is"))
# partition 永远返回三个部分
print("life is not all rose".partition("not"))  # 返回指定串前面的部分，指定串，指定串后面的部分（没有找到指定串返回源串及两个空格）

# split切片  按指定字符串切片，会丢失指定的串，可以指定次数，split() 默认空格
print("life is not all rose".split())
# splitlines 按行分割 \n  --"".splitlines(keepends=True) 保留换行符
print("life is not all rose\n my name".splitlines())
# join 指定符号连接字符串或可迭代的字符串对象
print(", ".join([str(x) for x in range(0, 11)]))
# replace 替换指定的字符串
print("life is not all rose".replace("life", "snow"))
# lower upper 转换成小写/大写
print("life is not all rose".upper())

# startswith 判断是否以指定的字符开始
print("life is not all rose".startswith("i", 1))
# endswith 判断是否以指定的字符结束
print("life is not all rose".endswith("rose",16))
# encode 字符串转化字节串(编码)
print("我是谁，王小明".encode("unicode_escape"))
# decode 字节串转换字符串(解码)
print(b'\xe6\x88\x91\xe6\x98\xaf\xe8\xb0\x81\xef\xbc\x8c\xe7\x8e\x8b\xe5\xb0\x8f\xe6\x98\x8e'
      .decode("utf-8", errors="ignore"))