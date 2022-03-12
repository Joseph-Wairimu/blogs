from flask import render_template,redirect,url_for, request, flash
from . import auth
from ..models import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from .. import db




@auth.route('/login')
def login():
  
    '''
    View root page function that returns the index page and its data
    '''
    
    
    return render_template('auth/login.html')   

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

  
    if user is not None and not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
   
    login_user(user, remember=remember)

    return redirect(url_for('main.index'))    


@auth.route('/signup')
def signup():

    '''
    View root page function that returns the index page and its data
    '''
    
    
    return render_template('auth/signup.html')


@auth.route('/signup',methods=['POST'])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')  
    
    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

   

    return redirect(url_for('auth.login'))
    title = "New Account"    


@auth.route('/logout')
@login_required
def logout():

    '''
    View root page function that returns the index page and its data
    '''
    
    logout_user()
    return redirect(url_for("main.index"))            

