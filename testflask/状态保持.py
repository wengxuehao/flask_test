# coding=utf-8

from flask import Flask, make_response, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'test'


# @app.route('/index')
# def index():
#     # 设置cookie和设置过期时间
#     response = make_response('this is set cookie')
#     response.set_cookie('username', 'itcast', max_age=1000)
#     return response


# 获取cookie，请求对象里面cookies，字典的get获取
# session作为请求上下文对象，用于处理http请求中的一些内容
@app.route('/cookie_get')
def cookie_get():
    response = request.cookies.get('username')
    return response


# 设置session,同时需要设置secret_key
@app.route('/index1')
def index1():
    session['username'] = 'itcast'
    return redirect(url_for('index'))


# 获取session中的数据
@app.route('/')
def index():
    return session.get('username')


if __name__ == '__main__':
    app.run()
