from flask import Flask
from flask import jsonify  # json序列化，数据体积小
import json


app = Flask(__name__)

# 避免中文乱码
app.config['JSON_AS_ASCII'] = False

dic = {'name': 'dyq', "age": 18}


@app.route('/jsonify')
def json_ify():
    # json格式序列化
    return jsonify(dic)  # 响应到页面上为json格式


@app.route('/json')
def json_da():
    return json.dumps(dic)  # 响应到页面上为text/html格式


if __name__ == '__main__':
    app.run()