import requests, pprint, json

# response = requests.get('http://mirrors.sohu.com/')
# print(response.status_code)  # 响应状态码

# 响应headers
response = requests.get('http://mirrors.sohu.com/')

print(type(response.headers))  # dict的子类

pprint.pprint(dict(response.headers))

# 获取消息体的文本内容，指定解码方式
response = requests.get('http://mirrors.sohu.com/')
response.encoding = 'utf8'
print(response.text)

# 获取消息体的字节串
response = requests.get('http://mirrors.sohu.com/')
print(response.content)

# 反序列化json格式为python对象
response = requests.post("http://httpbin.org/post", data={1: 1, 2: 2}).json().get('form').get('1')
# a = json.loads(response.content.decode())
# print(a)

print(response)
