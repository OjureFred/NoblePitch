from . import db
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class Pitch(db.Model):
    '''
    Pitch class to define Pitch objects and table
    '''
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True)
    description = db.Column(db.String(2000), index=True)
    category = db.Column(db.String(255), index=True)
    
    @classmethod
    def load_pitches():
        return Pitch.query.all()
    
    def __repr__(self):
        return f'Pitch - {self.title}'

class User(UserMixin, db.Model):
    '''
    Users class to define User objects and table
    '''
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")

    def __repr__(self):
        return f'User {self.username}'

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
class Role(db.Model):
    '''
    Class to define Role Object and table
    '''
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy = "dynamic")

    def __repr__(self):
        return f'Role {self.name}'

class Comment(db.Model):
    '''
    Funtion that defines Pitch comment
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String)
    pitch_comment = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_comments(cls, id):
        comment_list = Comment.query.filter_by(pith_id=id).all()
        return comment_list

