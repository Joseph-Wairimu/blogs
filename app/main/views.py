from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from .forms import UpdateProfile
from ..models import  User
#....

@main.route('/')
def index():
    
    return render_template('index.html')

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    '''
    View root page function that returns the index page and its data
    '''
    
    if user is None:
        abort(404)
    
    return render_template('profile/profile.html',user = user)       