from .database import db

class Pharmacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(20), nullable=False)