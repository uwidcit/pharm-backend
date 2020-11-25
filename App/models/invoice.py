from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.Integer, nullable = False)
    order_number = db.Column(db.Integer, db.ForeignKey('order.number'), nullable=False)
    
    def generateInvoice():
        return ""

    def updateInvoice():
        return ""
    
    def toDict(self):
        return ""
