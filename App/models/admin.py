#from flask_sqlalchemy import SQLAlchemy
from .database import db
from .user import User

class Admin(db.Model):    
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #user = db.relationship("User", backref="admin", uselist=False)
    
    type =  type = db.Column(db.String(50))
    
    '''def toDict(self):        
        user = User.query.get(id = self.user_id)
        return{
            'uwi_id': user.uwi_id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'type': self.type
        }'''
