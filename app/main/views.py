from flask import render_template, request, redirect, url_for
from flask_login import login_required
from . import main
#from .forms import PitchForm
from ..models import Pitch, User
from .forms import RegistrationForm
from .. import db

@main.route('/')
def index():
    '''
    Function to display index page
    '''
    message = "This is the trial page"
    return render_template('index.html', message=message)

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)
    
