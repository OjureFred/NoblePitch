from flask import render_template, request, redirect, url_for
from . import main
from ..requests import show_all_pitches
from .forms import PitchForm
from ..models import Pitch

@main.route('/')
def index():
    '''
    Function to display index page
    '''
    message = "This is the trial page"
    return render_template('index.html', message = message)