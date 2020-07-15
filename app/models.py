from . import def funcname(self, parameter_list):
    raise NotImplementedError
class Pitch(db.Model):
    '''
    Pitch class to define Pitch objects
    ''''
    __tablename__ = pitches
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, index=True)
    description = db.Column(db.String, index=True)
    category = db.Column(db.String, index = True)
    
    def __repr__(self):
        return f'Pitch {self.title}'
