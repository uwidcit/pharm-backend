from App.models import User
from App.models.database import db

def create_user(firstname, lastname, email, password, allergy, medications, role):
    newUser = User(first_name=firstname, last_name=lastname, email=email, allergies = allergy, medicines = medications, role = role)
    newUser.setPassword(password)
    db.session.add(newUser)
    db.session.commit()
    print("User successfully created")
    return newUser

def get_user(email):
    print("getting user")
    user = User.query.filter_by(email=email).first() # if this returns a user, then user is an admin
    return user

def get_users():
    print('get_users')
    users = User.query.all()
    list_of_users = []
    if users:
        list_of_users = [u.toDict() for u in users]
    return list_of_users