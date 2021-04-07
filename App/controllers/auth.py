from flask import redirect, render_template, request, session, url_for
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from App.models import User, Admin, Customer
from App.models.database import db
from datetime import datetime, timedelta

from flask import current_app

def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.checkPassword(password):
        return user

#Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return User.query.get(payload['identity'])