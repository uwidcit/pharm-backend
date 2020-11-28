from werkzeug.security import generate_password_hash, check_password_hash
from .database import db
from .user import User
class Customer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #user = db.relationship("User",uselist=False,backref= "customer")

    '''id = db.Column(db.Integer, primary_key=True)
    uwi_id = db.Column(db.Integer(), unique=True)
    first_name = db.Column(db.String(50), nullable=False) 
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(120))
    
    def encryptPassword(password): 
        return generate_password_hash(password, method="sha256")
    
    def checkPassword(self,password):
        return check_password_hash(self.password, password)

    def changePassword(self,password):
        self.password = encryptPassword(password)'''
    
    def toDict(self):
        return self.user.toDict()