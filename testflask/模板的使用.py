# coding=utf-8
from flask import Flask, render_template

app = Flask(__name__)


# 自定义过滤器
def do_listreverse(li):
    # 通过原列表创建一个新列表
    temp_li = list(li)
    # 将新列表进行返转
    temp_li.reverse()
    return temp_li


app.add_template_filter(do_listreverse, 'lireverse')


@app.route('/index')
def index():
    my_str = 'Hello 黑马程序员'
    my_int = 10
    my_array = [3, 4, 2, 1, 7, 9]
    my_dict = {
        'name': 'xiaoming',
        'age': 18
    }
    return render_template('template_demo1.html',
                           my_array=my_array,
                           my_str=my_str,
                           my_int=my_int,
                           my_dict=my_dict)


# 自定义过滤器
# @app.template_filter('lireverse')
# def do_listreverse(li):
#     # 通过原列表创建一个新列表
#     temp_li = list(li)
#     # 将新列表进行返转
#     temp_li.reverse()
#     return temp_li


if __name__ == '__main__':
    app.run(debug=True)
