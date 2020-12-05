from datetime import datetime
from .database import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    amount_paid = db.Column(db.Integer, nullable=False)
    date_paid = db.Column(db.DateTime(), nullable=False)

    def processPayment():
        return ""

    def updatePaymentStatus():
        return ""
    
    def toDict(self):
        return ""
