from .database import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Float, unique=True, nullable=False)
    product_name = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(300), nullable=False)     
    supplier_cost_price = db.Column(db.Float, nullable=False)
    supplier = db.Column(db.String(200), nullable = False)    
    QoH = db.Column(db.Float, nullable = False)
    stock_unit = db.Column(db.Float, nullable = False)
    unit_retail_price = db.Column(db.Float, nullable = False)
    total_retail_price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(300), nullable=True)
    
    def setPrice(self, price):
        self.unit_retail_price = price

    def toDict(self):
        return {
            "code": self.code,
            "product_name": self.product_name,
            "category": self.category,
            "supplier": self.supplier,
            "supplier_cost_price": self.supplier_cost_price,
            "QoH": self.QoH,
            "stock_unit": self.stock_unit,
            "unit_retail_price": self.unit_retail_price,
            "total_retail_price": self.total_retail_price,
            "image" : self.image,
        }
