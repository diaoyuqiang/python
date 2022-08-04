import requests
# 获取请求的原始响应：Response.raw、Response.iter_content
url = "http://wx4.sinaimg.cn/large/d030806aly1fq1vn8j0ajj21ho28bduy.jpg"

res = requests.get(url, stream=True)
with open('1.jpg', 'wb') as f:
    for t in res.iter_content(chunk_size=1024):  # 可以边下载边保存到文件中
        f.write(t)

url = "http://wx4.sinaimg.cn/large/d030806aly1fq1vn8j0ajj21ho28bduy.jpg"
r = requests.get(url, stream=True)
print(len(r.raw.read(10)))  # 流式读取10个bytes


