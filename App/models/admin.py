from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Admin(db.Model):    
    type =  type = db.Column(db.String(50))

    def createAdmin():
        return ""

    def changeType():
        return ""
    
    def toDict():
        return ""
