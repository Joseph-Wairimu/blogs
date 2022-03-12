from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms import validators
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you:',validators = [DataRequired()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
  title = StringField(' title:',validators=[DataRequired()]) 
  post = StringField(' post:',validators=[DataRequired()]) 
  username= StringField(' username:',validators=[DataRequired()])
  category = SelectField("Choose your desired category:",choices=[('interview_pitch','interview_pitch'),('pickup_lines','pickup_lines'),('product_pitch','product_pitch'),('promotion_pitch','promotion_pitch'),('Humour_pitch','Humour_pitch')])

  submit = SubmitField('Submit')
                                  