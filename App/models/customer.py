from .user import db
from . import User
class Customer(db.Model, User):

    '''id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", backref="admin", uselist=False)'''

    def createCustomer():
        return ""
    
    def toDict():
        return ""


