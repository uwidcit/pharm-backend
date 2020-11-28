from werkzeug.security import generate_password_hash, check_password_hash
from .database import db
from .user import User
class Customer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #user = db.relationship("User",uselist=False,backref= "customer")
        
    '''def toDict(self):
        user = User.query.filter_by(id = self.user_id)
        return {
            "uwi_id": user.uwi_id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }'''