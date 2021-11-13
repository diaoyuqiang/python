import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
r = requests.get('http://127.0.0.1:5000/index', headers=headers, timeout=0.01)

print(r.status_code)  # 状态码
print(r.text)