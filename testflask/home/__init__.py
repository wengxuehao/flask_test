#coding=utf-8
from flask import Blueprint
# 1 在模块的Init文件中创建蓝图对象，标注前缀
home_blu = Blueprint('home',__name__,url_prefix='/home')
# 导入views的内容
from .views import *
