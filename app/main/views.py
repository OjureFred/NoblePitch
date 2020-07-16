from flask import render_template, request, redirect, url_for
from flask_login import login_required
from . import main
#from .forms import PitchForm
from ..models import Pitch, User
from .. import db, photos

@main.route('/')
def index():
    '''
    Function to display index page
    '''
    pitch_list = Pitch.load_pitches()

    for pitch in pitch_list:
        print(pitch)
   
   return render_template('index.html', pitch_list=pitch_list)

@main.route('/usr/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

