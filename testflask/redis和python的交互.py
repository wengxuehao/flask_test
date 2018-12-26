# coding=utf-8
from redis import *

# 创建redis链接对象
sr = StrictRedis(host='localhost', port=6379, db=0)
