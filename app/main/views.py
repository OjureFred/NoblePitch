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
    
    return render_template('index.html', pitches=pitches)

