from flask import redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from App.models import User, Admin, Customer
from App.models.database import *

def log_in(uwi_id, pword):
    user = User.query.filter_by(uwi_id = uwi_id).first()
    pword = generate_password_hash(pword)
    if(user.check_password(pword)):
        print("Logged In Successfully")
    else: print("Wrong username or password. Please try again")
