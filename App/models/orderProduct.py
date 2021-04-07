from .database import db

class OrderProduct(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    product = db.relationship("Product", back_populates="orders")
    order = db.relationship("Order", back_populates="products")