from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class PrescriptionOrder(db.Model):
    image = db.Column(db.String(300), nullable=False)

    def createPrescriptionOrder():
        return ""
    
    def toDict():
        return ""
