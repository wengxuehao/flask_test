# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
# 创建管理对象
mgr = Manager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://wxh:wxh19950905@127.0.0.1:3306/test'
# 动态追踪修改设置，如未设置只会提示警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
# 创建数据库连接
db = SQLAlchemy(app)
# 初始化迁移器
Migrate(app, db)
# 生成迁移命令（使用管理器）
mgr.add_command(db, MigrateCommand)


# 定义模型Role
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(64), unique=True)


@app.route('/')
def index():
    user = User(name='zs')
    db.session.add(user)
    db.session.commit()
    return 'index'


if __name__ == '__main__':
    mgr.run()
