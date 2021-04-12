#from flask_sqlalchemy import SQLAlchemy
from .database import db
from .user import User

class Admin(db.Model):    
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", foreign_keys=[user_id])
    
    def toDict(self):
        return {
            'user': self.user.toDict(),
        }
