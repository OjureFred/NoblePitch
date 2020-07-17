from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import main
#from .forms import PitchForm
from ..models import Pitch, User
from .. import db 

@main.route('/')
def index():
    '''
    Function to display index page
    '''
    pitch_list = Pitch.query.all()

    for pitch in pitch_list:
        print(pitch)
   
    return render_template('index.html', pitch_list=pitch_list)

@main.route('/pitch/review/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitch = get_pitch(id)
    if form.validate_on_submit():
        title = form.title.data
        comment = form.review.data

        # Updated comment instance
        new_review = Review(movie_id=movie.id,movie_title=title,image_path=movie.poster,movie_review=review,user=current_user)

        # save review method
        new_review.save_review()
        return redirect(url_for('.movie',id = movie.id ))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)



