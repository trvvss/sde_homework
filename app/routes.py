from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    user = {'username': 'Travis'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)

@app.route('/users')
def users():
    user = {'username': 'Travis'}
    users = [
        {'username': 'Travis'},
        {'username': 'Bob'},
        {'username': 'Jimbo'},
        {'username': 'ZipZap'}
    ]
    return render_template('users.html', user=user, users=users)

@app.route('/books')
def books():
    return render_template('books.html')


@app.route('/authors')
def authors():
    return render_template('authors.html')