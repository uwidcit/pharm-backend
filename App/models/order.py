from .database import db
from datetime import datetime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship("Customer", foreign_keys=[customer_id])
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship("Product", foreign_keys=[product_id])
    item_count = db.Column(db.Integer, nullable=False)
    order_total = db.Column(db.Integer, nullable=False)
    date_placed = db.Column(db.DateTime, nullable=False)
    pickup_status = db.Column(db.String(50), nullable=False)
    
    def toDict(self):
        return{
            "order_number": self.order_number
        }