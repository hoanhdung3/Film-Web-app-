from datetime import datetime
from phim import db, login_manager
from flask_login import UserMixin
@login_manager.user_loader

def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(120), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image}')"

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_eng = db.Column(db.String(100), nullable=False)
    movie_vn = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    imdb = db.Column(db.Float, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    nation = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(120), nullable=False, default='default.png')
    link = db.Column(db.String(150), nullable=False)
    tl = db.Column(db.String(10), nullable=False)



    def __repr__(self):
        return f"Movie('{self.movie_eng}', '{self.movie_vn}', '{self.year}', '{self.imdb}', '{self.summary}', '{self.author}', '{self.nation}', '{self.image}', '{self.link}', '{self.tl}')"