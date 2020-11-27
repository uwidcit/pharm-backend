'''from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()'''
from datetime import datetime
from App.models.database import *

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship("customer", backref="order", uselist=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship("product", backref="order", uselist=False)
    item_count = db.Column(db.Integer, nullable=False)
    order_total = db.Column(db.Integer, nullable=False)
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id'), nullable=False)
    payment = db.relationship("payment", backref="order", uselist=False)
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
