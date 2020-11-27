'''from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()'''
from App.models.database import *
from App.models.order import Order

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.Integer, nullable = False)
    #order_number = db.Column(db.Integer, db.ForeignKey('Order.order_number'), nullable=False)
    
    def generateInvoice():
        return ""

    def updateInvoice():
        return ""
    
    def toDict(self):
        return ""
