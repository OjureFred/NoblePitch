from flask import render_template, request, redirect, url_for
from . import main
from ..requests import show_all_pitches
from .forms import PitchForm
from ..models import Pitch