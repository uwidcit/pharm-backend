from .database import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uwi_id = db.Column(db.Integer(), unique=True)
    first_name = db.Column(db.String(50), nullable=False) 
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(120))
    token = db.Column(db.String(50))
    
    def setPassword(self, password): 
        self.password = generate_password_hash(password, method="sha256")
    
    def checkPassword(self,password):
        return check_password_hash(self.password, password)
    
    def toDict(self):
        return{

            'uwi_id': self.uwi_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
