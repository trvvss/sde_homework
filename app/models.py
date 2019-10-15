from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    

    def __repr__(self):
        return f"User('{self.first_name}, '{self.last_name}', {self.email}')"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    title = db.Column(db.String(120), unique=True, nullable=False)
    isbn = db.Column(db.Integer, unique=True, nullable=False)
    year_published = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author_id}', '{self.isbn}', '{self.year_published}')"

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=True)
    books = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f"Author('{self.first_name}, '{self.last_name}')"

# class Wishlist(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
#     last_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

#     def __repr__(self):
#         return f"Wishlist('{self.user_id}, '{self.book_id}', '{self.last_updated}')"