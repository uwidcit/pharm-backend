from flask import redirect, render_template, request, session, url_for

from App.models import User
from App.models.database import db

def create_user( uwiid, firstname, lastname, email, password):
    newUser = User(uwi_id=uwiid, first_name=firstname, last_name=lastname, email=email)
    newUser.setPassword(password)
    db.session.add(newUser)
    db.session.commit()
    print("Successfully created")
    return newUser

def get_users():
    print('get_users')
    users = User.query.all()
    list_of_users = []
    if users:
        list_of_users = [u.toDict() for u in users]
    return list_of_users