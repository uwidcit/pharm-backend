#from flask_sqlalchemy import SQLAlchemy
from .database import db
from .user import User

class Admin(db.Model):    
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", foreign_keys=[user_id])
    
    type =  type = db.Column(db.String(50))
    
    def toDict(self):        
        return{
            'uwi_id': self.user.uwi_id,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'email': self.user.email,
            'type': self.type
        }
