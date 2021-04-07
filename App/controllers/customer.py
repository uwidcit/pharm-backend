from flask import redirect, render_template, request, session, url_for

from App.models import ( Customer )
from App.models.database import db

def create_customer(newUser, allergy, medications):
    newCust = Customer(user_id = newUser.id, allergies = allergy, medicines = medications)
    db.session.add(newCust)
    db.session.commit()
    print("Successfully Created")
    return newCust

def get_customers():
    print('get all customers')
    customers = Customer.query.all()
    list_of_customers = []
    if customers:
        list_of_customers = [c.toDict() for c in customers]
    return list_of_customers

def get_customer(id):
    print("getting user")
    user = Customer.query.filter(id == id).first() # if this returns a user, then the email already exists in database
    return user

def get_customers_by_term(term):
    list_of_customers = []
    customers = Customer.query.filter(
        Customer.allergies.contains(term) 
        | Customer.medicines.contains(term) 
        | Customer.user.has(email = term)
        | Customer.user.has(first_name = term)
        | Customer.user.has(last_name = term)
    )
    if customers:
        list_of_customers = [c.toDict() for c in customers]
    return list_of_customers