from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms import ValidationError
from wtforms.validators import Required

class CommentForm(FlaskForm):

    pitch_comment = TextAreaField('Comment', validators=[Required()])
    user_id = StringField('User ID')
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    pitch_title = StringField('Pitch', validators=[Required()])
    pitch_description = TextAreaField('Description', validators=[Required()])
    pitch_category = StringField('Category', validators=[Required()])
    submit = SubmitField('Submit')