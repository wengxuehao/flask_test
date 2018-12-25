# coding=utf-8
from flask import Flask, request, make_response, jsonify, redirect, url_for, abort

app = Flask(__name__)


@app.route('/')
def index():
    return '这是首页界面'


# @app.route('/')
# def index():
#     response = make_response("hello flask")  # type: Response
#     # print(response.headers)  # 响应头信息
#     # print(response.content_type)  # 响应的content-type    默认为 text/html 返回网页
#     response.headers = {
#         "Content - Encoding": "gzip"
#     }
#     print(response.headers)
#     return response  # 返回自定义的响应对象


# # 返回json类型字符串
# @app.route('/demo', methods=['GET'])
# def demo():
#     json_dict = {
#         "user_id": 10,
#         "user_name": "laowang"
#     }
#     return jsonify(json_dict)


# @app.route('/demo2')
# def demo2():
#     # 重定向
#     return redirect('http://www.baidu.com')


# 重定向到自己编写的url
# @app.route('/demo3')
# def demo3():
#     return redirect(url_for('demo2'))


# 路由传递参数
# @app.route('/user/<int:user_id>')
# def user_info(user_id):
#     return 'hello %d' % user_id


# # 重定向
# @app.route('/demo5')
# def demo5():
#     # 使用 url_for 生成指定视图函数所对应的 url
#     return redirect(url_for('user_info', user_id=100))


# 自定义状态密码
# @app.route('/demo6')
# def demo6():
#     # abort(400)
#     return '状态码为 555'


# @app.errorhandler(500)
# @app.route('/demo7')
# def internal_server_error(e):
#     return '服务器搬家了'


# @app.errorhandler(ZeroDivisionError)
# # 捕获指定错误
# def zero_division_error(e):
#     return '除数不能为0'

if __name__ == '__main__':
    app.run(debug=True)
