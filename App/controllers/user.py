from flask import redirect, render_template, request, session, url_for

from App.models import User
from App.models.database import db

def create_user( uwi_id, firstname, lastname, email, password):
    password = User.encryptPassword(password)
    newUser = User(uwi_id = uwi_id, first_name=firstname, last_name = lastname, email = email, password = password)
    db.session.add(newUser)
    db.session.commit()
    print("Successfully created")
    return newUser