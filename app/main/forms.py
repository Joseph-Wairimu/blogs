from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms import validators
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you:',validators = [DataRequired()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
  
  title = StringField(' About:',validators=[DataRequired()]) 
  post = TextAreaField('Blog Description:',validators=[DataRequired()]) 
  username= StringField(' Author:',validators=[DataRequired()])
  category = SelectField("Choose your desired category:",choices=  [ ('Personal_blogs','Personal_blogs'), ('corporate_blogs','corporate_blogs'), ('Fashion_blogs','Fashion_blogs'),('Lifestyle_blogs','Lifestyle_blogs'),('Travel_blogs','Travel_blogs')] )
  submit = SubmitField('Submit')

                                  