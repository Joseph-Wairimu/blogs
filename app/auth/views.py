from flask import render_template,redirect,url_for, request, flash
from . import auth




@auth.route('/login')
def login():
  
    '''
    View root page function that returns the index page and its data
    '''
    
    
    return render_template('auth/login.html')    
