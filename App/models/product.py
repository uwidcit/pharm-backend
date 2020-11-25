from .user import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(300))
    unit_price = db.Column(db.Integer, nullable=False)

    def setDescription(self, desc):
        self.description = desc

    def setImage(self, img):
        self.image = img
    
    def setPrice(self, price):
        self.unit_price = price

    def toDict(self):
        return {
            'name': self.name,
            'description': self.description,
            'image': self.image,
            'unit_price': self.unit_price
        }
