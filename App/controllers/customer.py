from flask import redirect, render_template, request, session, url_for

from App.models import ( Customer )
from App.models.database import *

def create_customer(newUser):
    newCust = Customer(user_id = newUser.id)
    db.session.add(newCust)
    db.session.commit()
    print("Customer successfully created")
    return newCust