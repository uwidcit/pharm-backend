from flask import redirect, render_template, request, session, url_for

from App.models import ( Admin )
from App.models.database import db

def create_admin(newUser):
    newAdmin = Admin(user_id = newUser.id)
    db.session.add(newAdmin)
    db.session.commit()
    print("Admin successfully Created")
    return newAdmin