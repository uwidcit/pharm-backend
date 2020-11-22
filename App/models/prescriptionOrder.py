from . import db
from . import Order

class PrescriptionOrder(db.Model, Order):
    image = db.Column(db.String(300), nullable=False)

    def createPrescriptionOrder():
        return ""
    
    def toDict():
        return ""
