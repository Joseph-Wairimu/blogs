from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    email=db.Column(db.String(255),unique = True)
    password=db.Column(db.String(255))
    username = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())



     
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    post = db.Column(db.String(255))
    category = db.Column(db.String(255))
    title = db.Column(db.String(255))
    vote_count = db.Column(db.Integer)
    added_date = db.Column(db.DateTime,default=datetime.utcnow)
    author = db.Column(db.Integer,db.ForeignKey('users.id'))

