from . import db 

class Pitch(db.Model):
    '''
    Pitch class to define Pitch objects and table
    '''
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True)
    description = db.Column(db.String(255), index=True)
    category = db.Column(db.String(255), index = True)
    
    def __repr__(self):
        return f'Pitch {self.title}'

class User(db.Model):
    '''
    Users class to define User objects and table
    '''
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    '''
    Class to define Role Object and table
    '''

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy = "dynamic")

    def __repr__(self):
        return f'Role {self.name}'

