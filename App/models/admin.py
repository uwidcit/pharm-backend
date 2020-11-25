from . import User
from .user import db

class Admin(db.Model, User):
    
    type =  type = db.Column(db.String(50))

    def createAdmin():
        return ""

    def changeType():
        return ""
    
    def toDict():
        return ""
