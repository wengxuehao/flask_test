#coding=utf-8

from flask import Flask

from testflask.home import home_blu

app = Flask(__name__)
# 在项目文件中注册蓝图
app.register_blueprint(home_blu)


if __name__ == '__main__':
    app.run(debug=True)