from flask import Flask
app = Flask(__name__)  # 创建fFlask应用


@app.route('/index/<user>', methods=['POST'])  # 设置路由并接收参数
def hello(user):
    return 'hello world %s!' % user


if __name__ == "__main__":
    app.run(debug=True)