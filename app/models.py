from . import db
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Pitch(db.Model):
    '''
    Pitch class to define Pitch objects and table
    '''
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True)
    description = db.Column(db.String(2000), index=True)
    category = db.Column(db.String(255), index=True)
    
    def load_pitches():
        return Pitch.query.all()
    
    def __repr__(self):
        return f'Pitch {self.title}'

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

