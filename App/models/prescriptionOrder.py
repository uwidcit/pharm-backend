from datetime import datetime
from .database import db
from .order import Order

class PrescriptionOrder(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    #order = db.relationship("order", backref="prescriptionOrder", uselist=False)
    image = db.Column(db.String(300), nullable=False)

    def createPrescriptionOrder():
        return ""

    def toDict(self):
        return ""

