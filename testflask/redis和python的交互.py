# coding=utf-8
from redis import *

if __name__ == "__main__":
    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        # 指定参数host、port与指定的服务器和端⼝连接，host默认为localhost，port默认为6379，db默认为0，password指明登录密码
        sr = StrictRedis(password='12345')
        # 添加键name，值为itheima
        result = sr.set('name', 'itheima')
        # 输出响应结果，如果添加成功则返回True，否则返回False
        print(result)
        get = sr.get('name')
        # 输出键对应的值，如果不存在返回none
        print(get.decode('utf-8'))
        xiugai = sr.set('name','zhangsan')
        print(xiugai)
        print(sr.get('name').decode('utf-8'))
    except Exception as e:
        print(e)
