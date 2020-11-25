from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uwi_id = db.Column(db.Integer(), unique=True)
    first_name = db.Column(db.String(50), nullable=False) 
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(120))

    def createUser():
        return ""

    def checkPassword():
        return ""

    def changePassword():
        return ""
    
    def toDict(self):
        return{
            'id': self.id,
            'uwi_id': self.uwi_id,
        }
