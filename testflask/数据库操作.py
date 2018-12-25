# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://wxh:wxh19950905@127.0.0.1:3306/test'
# 动态追踪修改设置，如未设置只会提示警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
# 创建数据库连接
db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = "users"  # 默认使用类名的小写做表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)


@app.route('/index')
def index():
    # 删除所有表
    db.drop_all()
    # 创建所有继承自db.Model的表
    db.create_all()
    # 创建模型
    user = User(name="zs")

    # 添加数据 到会话中
    db.session.add(user)
    # 会话提交(提交后, 才会执行数据库操作)
    db.session.commit()

    # # 修改数据
    # user.name = "wangwu"
    # db.session.commit()

    # 删除数据
    db.session.delete(user)
    db.session.commit()

    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
