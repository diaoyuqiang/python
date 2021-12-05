import requests
import pprint

# # 传递url请求参数的方式
# paras = {
#     'wd': 'iphone',
#     'rsv+spt': '1'
# }
#
# res = requests.get('http://www.baidu.com/s', params=paras)
# pprint.pprint(res.text)

# # xml格式消息体
# payload = '''
# <?xml version="1.0" encoding="UTF-8"?>
# <WorkReport>
#     <Overall>良好</Overall>
#     <Progress>30%</Progress>
#     <Problems>暂无</Problems>
# </WorkReport>
# '''
#
# r = requests.post("http://httpbin.org/post",  # http://httpbin.org :resqurest测试网站
#                   data=payload.encode('utf8'))  # data: 传递消息体，指定编码方式
# print(r.text)


# # urlencoded格式消息体
# payload = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# json格式消息体
payload = {
    "Overall": "良好",
    "Progress": "30%",
    "Problems": [
        {
            "No": 1,
            "desc": "问题1...."
        },
        {
            "No": 2,
            "desc": "问题2...."
        },
    ]
}

r = requests.post("http://httpbin.org/post", json=payload)
print(r.text)