import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'libris_project'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/books')
def books_page():
    return render_template("books.html", books=mongo.db.books.find(), reviews=mongo.db.books_comments.find())


@app.route('/add_book')
def add_book():
    return render_template('addbook.html')


@app.route('/insert_book', methods=['POST'])
def insert_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('books_page'))


@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template('editbook.html', book=the_book)


@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    books = mongo.db.books
    books.update({'_id': ObjectId(book_id)},
        {
            'book_title': request.form.get('book_title'),
            'cover_photo': request.form.get('cover_photo'),
            'author': request.form.get('author'),
            'year': request.form.get('year'),
            'synopsis': request.form.get('synopsis'),
            'collection': request.form.get('collection'),
            'genre': request.form.get('genre')
        })
    return redirect(url_for('books_page'))


@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('books_page'))


@app.route('/posts')
def posts_page():
    return render_template("posts.html", posts=mongo.db.posts.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)