from .database import db
from .order import Order

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.Integer, nullable = False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    order = db.relationship("Order", foreign_keys=[order_id])
    
    def toDict(self):
        return {
            "invoice_number": self.invoice_number,
            "order_number": self.order.order_number
        }
