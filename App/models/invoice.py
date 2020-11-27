'''from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()'''
from App.models.database import *
from App.models.order import Order

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.Integer, nullable = False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    order = db.relationship("order", backref="invoice", uselist=False)

    def generateInvoice():
        return ""

    def updateInvoice():
        return ""
    
    def toDict(self):
        return ""
