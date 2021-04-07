from .database import db
from datetime import datetime
import json

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="orders")
    item_count = db.Column(db.Integer, nullable=False)
    order_total = db.Column(db.Integer, nullable=False)
    date_placed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    pickup_status = db.Column(db.String(50), nullable=False)
    products = db.relationship("OrderProduct", back_populates="order")

    def toDict(self):
        return{
            "id" : self.id,
            "user" : self.user.toDict(),
            "item_count": self.item_count,
            "order_total": self.order_total,
            "date_placed": self.date_placed.strftime("%a, %d %b, %Y"),
            "status": self.pickup_status,
            "products": [OrderProduct.product.toDict() for OrderProduct in self.products]
        }