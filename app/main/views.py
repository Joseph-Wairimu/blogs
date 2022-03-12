from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from .forms import UpdateProfile,BlogForm,CommentForm
from ..models import  User,Post,Comment
from .. import db
from flask.helpers import flash
#....

@main.route('/')
def index():
    Personal_blogs= Post.query.filter_by(category='Personal_blogs').all()
    corporate_blogs = Post.query.filter_by(category='corporate blogs').all()
    Fashion_blogs= Post.query.filter_by(category='Fashion blogs').all()
    Lifestyle_blogs = Post.query.filter_by(category='Lifestyle blogs').all()
    Travel_blogs = Post.query.filter_by(category='Travel_blogs').all()
    posts = Post.query.order_by(Post.added_date.desc()).all()
    return render_template('index.html',Personal_blogs=Personal_blogs, corporate_blogs= corporate_blogs, Fashion_blogs= Fashion_blogs,Lifestyle_blogs=Lifestyle_blogs,Travel_blogs=Travel_blogs, posts=posts)


                   
                   

@main.route('/posts')
@login_required
def posts():

    Personal_blogs= Post.query.filter_by(category='Personal_blogs').all()
    corporate_blogs = Post.query.filter_by(category='corporate_blogs').all()
    Fashion_blogs= Post.query.filter_by(category='Fashion_blogs').all()
    Lifestyle_blogs = Post.query.filter_by(category='Lifestyle_blogs').all()
    Travel_blogs = Post.query.filter_by(category='Travel_blogs').all()
    posts = Post.query.order_by(Post.added_date.desc()).all()
    return render_template('blog.html',Personal_blogs=Personal_blogs, corporate_blogs= corporate_blogs, Fashion_blogs= Fashion_blogs,Lifestyle_blogs=Lifestyle_blogs,Travel_blogs=Travel_blogs, posts=posts)

@main.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user._get_current_object().id
      
        new_post=Post(title=title,post=post,category=category )
        new_post.save()
        db.session.add(new_post)
        db.session.commit()
        # post_obj.save()
        flash('Your blog has been created successfully!')
        return redirect(url_for('.posts',uname=current_user.username))
    return render_template('recent_blog.html', form=form ,title='Blog ')

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    author = current_user._get_current_object().id
    posts = Post.query.filter_by(author = author).all()
    '''
    View root page function that returns the index page and its data
    '''
    
    if user is None:
        abort(404)
    
    return render_template('profile/profile.html',user = user,posts=posts) 


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

    return render_template('profile/update.html',form =form,posts=posts)         


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

@main.route('/comment/<int:post_id>', methods=['GET', 'POST'])
@login_required
def comment(post_id):
    form = CommentForm()
    post = Post.query.get(post_id)
    user = User.query.all()
    comments = Comment.query.filter_by(post_id=post_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        post_id = post_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(
            comment=comment,
            post_id=post_id,
            user_id=user_id
        )
        new_comment.save_comment()
        new_comments = [new_comment]
        print(new_comments)
       
        return redirect(url_for('.comment', post_id=post_id))
    return render_template('comments.html', form=form, post=post, comments=comments, user=user)




