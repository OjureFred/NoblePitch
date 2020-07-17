from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms import ValidationError
from wtforms.validators import Required

class CommentForm(FlaskForm):

    pitch_comment = TextAreaField('Comment', validators=[Required()])
    user_id = StringField('User ID')
    submit = SubmitField('Submit')