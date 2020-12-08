from .database import db
from datetime import datetime

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    cart = db.relationship("Cart", foreign_keys=[cart_id])
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship("Product", foreign_keys=[product_id])
    quantity = db.Column(db.Integer, nullable=False)
    
    def toDict(self):
        return{
            'id': self.id,
            'cart_id': self.cart_id,
            'product_id': self.product_id,
            'quantity': self.quantity
        }