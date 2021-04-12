from flask import redirect, render_template, request, session, url_for

from App.models import ( User )
from App.models.database import db

def get_customers():
    print('get all customers')
    customers = User.query.filter_by(role = 1)
    list_of_customers = []
    if customers:
        list_of_customers = [c.toDict() for c in customers]
    return list_of_customers

def get_customers_by_term(term):
    list_of_customers = []
    customers = User.query.filter(
        (User.role.contains(1)) &
        (User.allergies.contains(term) 
        | User.medicines.contains(term) 
        | User.email.contains(term)
        | User.first_name.contains(term)
        | User.last_name.contains(term))
    )
    if customers:
        list_of_customers = [c.toDict() for c in customers]
    return list_of_customers

def delete_customer_by_id(customer_id):
    print("deleting customer")
    customer = User.query.filter(User.id == customer_id).first()
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return True
    return False