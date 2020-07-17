from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import main
import markdown2
from .forms import CommentForm
from ..models import Pitch, User, Comment
from .. import db 

@main.route('/')
def index():
    '''
    Function to display index page
    '''
    pitch_list = Pitch.query.all()

       
    return render_template('index.html', pitch_list=pitch_list)

@main.route('/pitch/comment/new/<int:id>', methods=['GET', 'POST'])
def new_comment(id):
    '''
    Function to allow a user add a comment
    '''
    form = CommentForm()
    if form.validate_on_submit():
       # Updated comment instance
       new_comment = Comment(pitch_id = id, pitch_comment = form.pitch_comment.data, user_id = form.user_id.data)

       # save comment method
       db.session.add(new_comment)
       db.session.commit()
       return redirect(url_for('main.index'))

    title = 'New comment'
    return render_template('new_comment.html', title=title)
    
@main.route('/pitch/<int:id>', methods=['GET', 'POST'])
def list_comments(id):
    '''
    Function to retrieve comment for a pitch
    '''
    pitch = Pitch.query.filter_by(id=id).first()
    comments = Comment.query.filter_by(pitch_id=id).all()
    
    return render_template('comments.html', pitch=pitch, comments=comments)
    
@main.route('/comment/<int:id>')
def single_comment(id):
    comment = Comment.query.get(id)
    if comment is None:
        abort(404)

    format_comment = markdown2.markdown(comment.pitch_comment, extras=["code-friendly", "fenced-code-blocks"])
    return render_template('comment_r.html', comment = comment, format_comment = format_comment)





