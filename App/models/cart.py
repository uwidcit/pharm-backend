from .database import db
from datetime import datetime

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship("Customer", foreign_keys=[customer_id])
    date_created = db.Column(db.DateTime(), default=datetime.now())
    checked_out = db.Column(db.Boolean, default=False)

    def toDict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'date_created': self.date_created,
            'checked_out': self.checked_out
        }