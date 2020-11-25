from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Admin(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    uwi_id = db.Column(db.Integer(), unique=True)
    first_name = db.Column(db.String(50), nullable=False) 
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(120))
    type =  type = db.Column(db.String(50))
    
    def encryptPassword(password): 
        return generate_password_hash(password, method="sha256")
    
    def checkPassword(self,password):
        return check_password_hash(self.password, password)

    def changePassword(self,password):
        self.password = encryptPassword(password)
    
    def toDict(self):
        return{

            'uwi_id': self.uwi_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
