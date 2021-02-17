from werkzeug.security import generate_password_hash, check_password_hash
from .database import db
from .user import User
class Customer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", foreign_keys=[user_id])
    DOB = db.Column(db.DateTime, nullable = False)
    allergies = db.Column(db.String(255))
    medicines = db.Column(db.String(255))
        
    def toDict(self):
        return {
            'user': self.user,
            'DOB': self.DOB,
            'allergies': self.allergies,
            'medicines' : self.medicines
        }