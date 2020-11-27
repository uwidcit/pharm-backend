'''from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()'''
from datetime import datetime
from App.models.database import *

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    item_count = db.Column(db.Integer, nullable=False)
    order_total = db.Column(db.Integer, nullable=False)
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id'), nullable=False)
    date_placed = db.Column(db.DateTime(), nullable=False)
    collection_status = status = db.Column(db.String(50), nullable=False)

    def placeOrder():
        return ""

    def updateOrder():
        return ""
    
    def cancelOrder():
        return ""

    def toDict(self):
        return ""
