from flask import redirect, render_template, request, session, url_for

from App.models import User, Admin, Customer
from App.models.database import db

def create_user(firstname, lastname, email, password):
    newUser = User(first_name=firstname, last_name=lastname, email=email)
    newUser.setPassword(password)
    db.session.add(newUser)
    db.session.commit()
    print("User successfully created")
    return newUser

def get_user_details(email):
    print("getting user")
    user = Admin.query.filter_by(email=email).first() # if this returns a user, then user is an admin
    if (user == None) :
        user = Customer.query.filter_by(email=email).first() # else returns a user if it is a customer
    return user

def get_users():
    print('get_users')
    users = User.query.all()
    list_of_users = []
    if users:
        list_of_users = [u.toDict() for u in users]
    return list_of_users

def get_user():
    print('get all user')
    users = User.query.all()
    list_of_users = []
    if users:
        list_of_users = [u.toDict() for u in users]
    return list_of_users
