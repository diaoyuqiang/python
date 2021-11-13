# unicode码
s = '\\u6211\\u559c\\u6b22\\u4f60'


# unicode解码
print(s.encode('utf8').decode('unicode_escape'))

# 转换成utf-8编码
print(s.encode('utf8').decode('unicode_escape').encode('utf8'))
