#Not in use yet as payment is not a feature available for project scope
from datetime import datetime
from .database import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    order = db.relationship('Order', backref='payment', lazy=True) 
    timestamp = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    
    def toDict(self):
        return {
            "id": self.id,
            "order": self.order.toDict(),
            "timestamp": self.timestamp
        }
