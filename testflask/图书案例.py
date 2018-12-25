# coding=utf-8
from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://wxh:wxh19950905@127.0.0.1:3306/test'
# 动态追踪修改设置，如未设置只会提示警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 查询时会显示原始SQL语句
# app.config['SQLALCHEMY_ECHO'] = True
# 创建数据库连接
db = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = "authors"  # 设置表名 表名默认为类名的小写
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 创建关系属性
    books = db.relationship("Book", backref="author")


# 书表  多
class Book(db.Model):
    __tablename__ = "books"  # 设置表名 表名默认为类名的小写
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 设置外键
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # 查询所有的作者并返回模板渲染
        try:
            authors = Author.query.all()
        except BaseException as e:
            flash('数据库异常')
            return redirect(url_for('index'))

        return render_template('book_test.html', authors=authors)

    # 请求方式是post的处理操作
    # 获取参数校验参数
    author_name = request.form.get('author_name')
    book_name = request.form.get('book_name')
    if not all([author_name, book_name]):
        flash('参数不足')
        return redirect(url_for('index'))
    book = Book.query.filter_by(name=book_name).first()
    # 判断书籍
    if book:
        flash('书籍已经存在')
        return redirect(url_for('index'))
    # 判断作者
    author = Author.query.filter_by(name=author_name).first()
    try:
        if author:
            # 创建书籍对象添加到作者
            book = Book(name=book_name)
            author.books.append(book)
            db.session.add(book)
            db.session.commit()
        else:
            # 没有当前作者和书籍都新创建新的
            new_book = Book(name=book_name)
            new_author = Author(name=author_name)
            new_author.books.append(new_book)
            db.session.add_all([new_book, new_author])
            db.session.commit()
    except BaseException as e:
        # 数据库操作都需要回滚
        db.session.rollback()
        print(e)
        flash('数据库操作错误')
        return redirect(url_for('index'))

    return redirect(url_for('index'))


# 删除书籍 先删除多的
# 动态url删除
@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    # 根据书籍id取出该书籍
    book = Book.query.get(book_id)
    # 将书籍从数据库中删除
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("index"))


# 删除作者，删除作者对应得书籍
@app.route('/delete_author/<int:author_id>')
def delete_author(author_id):
    # 根据作者id取出该作者
    author = Author.query.get(author_id)
    # 删除一对多的关联数据时, 先删多的一方, 再删除一的一方
    for book in author.books:
        db.session.delete(book)

    db.session.delete(author)
    db.session.commit()
    # Book.query.filter_by(author_id=author.id).delete()  # 也可以删除作者所有的书籍

    return redirect(url_for("index"))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    # 创建三个作者对象
    au1 = Author(name='老王')
    au2 = Author(name='老张')
    au3 = Author(name='老李')
    db.session.add_all([au1, au2, au3])
    db.session.commit()
    # 创建书籍对象bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()
    app.run(debug=True)
