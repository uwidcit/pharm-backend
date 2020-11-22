from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(300))
    unit_price = db.Column(db.Integer, nullable=False)

    def addProduct():
        return ""

    def updateProduct():
        return ""

    def deleteProduct():
        return ""

    def toDict(self):
        return ""