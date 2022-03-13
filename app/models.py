from . import db
from . import login_manager
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime



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
    username = db.Column(db.String(255))
    vote_count = db.Column(db.Integer)
    added_date = db.Column(db.DateTime,default=datetime.utcnow)
    author = db.Column(db.Integer,db.ForeignKey('users.id'))

    
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"   


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text(), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()
    def __repr__(self):
        return f'Comment: {self.comment}'  


       
        
class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_subscribers(cls):
        subscribers = Subscriber.query.all()
        return subscribers

    def __repr__(self):
        return f'Subscriber {self.email}'               