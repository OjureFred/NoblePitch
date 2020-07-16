from flask import render_template, request, redirect, url_for
from flask_login import login_required
from . import main
#from .forms import PitchForm
from ..models import Pitch, User
from .. import db 

@main.route('/')
def index():
    '''
    Function to display index page
    '''
    pitch_list = Pitch.load_pitches()

    for pitch in pitch_list:
        print(pitch)
   
    return render_template('index.html', pitch_list=pitch_list)



