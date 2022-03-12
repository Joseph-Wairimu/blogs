from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from .forms import UpdateProfile
from ..models import  User,Post
from .. import db
#....

@main.route('/')
def index():
    
    return render_template('index.html')



@main.route('/posts')
@login_required
def posts():
    posts = Post.query.all()
    user = current_user
    return render_template('blog.html', posts=posts, user=user)


@main.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user._get_current_object().id
      
        new_post=Post(title=title,post=post,category=category)
        new_post.save()
        db.session.add(new_post)
        db.session.commit()
        # post_obj.save()
        flash('Your pitch has been created successfully!')
        return redirect(url_for('main.index',uname=current_user.username))
    return render_template('recent_blog.html', form=form ,title='Pitch Perfect')

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


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)         


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))  
