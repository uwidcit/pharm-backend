from .database import db
from .order import Order

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.Integer, nullable = False)
    
    def toDict(self):
        return {
            "invoice_number": self.invoice_number,
        }
