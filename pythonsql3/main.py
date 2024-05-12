import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# db=sqlite3.connect("books-collection.db")
#
# cursor=db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
# #                "NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1,'Harry potter', 'J.K.viking', '9.3')")
# db.commit()
# app=Flask(__name__)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#
# db=SQLAlchemy()
# db.init_app(app)
#
#
# class Book(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     title=db.Column(db.String(250), unique=True, nullable=False)
#     author=db.Column(db.String(250), nullable=False)
#     rating=db.Column(db.Float, nullable=False)
# #
# #
# # with app.app_context():
# #     db.create_all()
#
# # with app.app_context():
# #     new_book=Book(id=1, title="harry potter", author="j,k viking",rating=3.4)
# #     db.session.add(new_book)
# #     db.session.commit()
#
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "harry potter")).scalar()
#
# with app.app_context():
#     bbok_update=db.session.execute(db.select(Book).where(Book.title=="harry potter")).scalar()
#     bbok_update.title="harry peter"
#     db.session.commit()





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db=SQLAlchemy()
db.init_app(app)


all_books = []


@app.route('/')
def home():
    result=db.session.execute()
    return render_template("index.html", added_books=all_books)


@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        new_bok={
            "title":request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_bok)
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)