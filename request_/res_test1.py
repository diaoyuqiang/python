import requests
import pickle, json
from PIL import Image  # 图像处理
from io import BytesIO  # 字节内存io
from flask import Flask, request

# payload = {'name': 'dyq', 'age': 18}
# r = requests.get('https://github.com/timeline.json', payload)  # 为url传递参数
# print(r.url)  # 输出请求的url
# a = r.json()  # python字典类型
# print(type(a), a)

# r1 = requests.get('http://i0.hdslb.com/bfs/archive/9e5f278027ae7f1e1933b6e4002870361da6c20b.png')
# i = Image.open(BytesIO(r1.content))  # 通过字节io变成图片对象加载到内存
# i.show()  # 显示图片
#
#
# ss = StringIO("Hello!\nGoodBay!")  # 读取StringIO内存只中
# print(ss.read())
# ss.close()

app = Flask('dyq')


@app.route('/index', methods=['POST', 'GET'])
def index():
    print(request.headers)
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)