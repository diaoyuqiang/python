import requests
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
print(r.json())  # 读取相应内容(转换成python字典类型)
print(r.text)  # 文本格式
