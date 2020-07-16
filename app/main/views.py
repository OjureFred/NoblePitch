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
    pitches = Pitch.load_pitches()
    print(pitches)
    testtext = "Let me see if this works"

    return render_template('index.html', testtext = testtext, pitches = pitches)

