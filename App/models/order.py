from .database import db
from datetime import datetime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    #customer = db.relationship("Customer", backref="order", uselist=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    #product = db.relationship("Product", backref="order", uselist=False)
    item_count = db.Column(db.Integer, nullable=False)
    order_total = db.Column(db.Integer, nullable=False)
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id'), nullable=False)
    #payment = db.relationship("Payment", backref="order", uselist=False)
    date_placed = db.Column(db.DateTime(), nullable=False)
    pickup_status = status = db.Column(db.String(50), nullable=False)