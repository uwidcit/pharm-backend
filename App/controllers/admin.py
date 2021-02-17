from flask import redirect, render_template, request, session, url_for

from App.models import ( Admin )
from App.models.database import db

def create_admin(newUser, type):
    newAdmin = Admin(user_id = newUser.id, type = type)
    db.session.add(newAdmin)
    db.session.commit()
    print("Admin successfully Created")
    return newAdmin