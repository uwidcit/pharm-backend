from flask import redirect, render_template, request, session, url_for

from App.models import ( Admin )
from App.models.database import *

def create_admin(newUser, type):
    newAdmin = Admin(user_id = newUser.id, type = type)
    db.session.add(newAdmin)
    db.session.commit()
    print("Successfully Created")
    return newAdmin