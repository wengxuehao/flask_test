#coding=utf-8


# 使用蓝图来注册路由不使用app
from testflask.home import home_blu


@home_blu.route('/')
def index():
    return 'index'
