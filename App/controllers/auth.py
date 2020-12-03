from flask import redirect, render_template, request, session, url_for
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from App.models import User, Admin, Customer
from App.models.database import *
from datetime import datetime, timedelta

from flask import current_app

def authenticate(uwi_id, password):
    print('Auth controller authenticate')

    user = User.query.filter_by(uwi_id=uwi_id).first()

    if user and user.checkPassword(password):
        print('Valid user')
        token = jwt.encode({ 
            'user': user.uwi_id, 
            'exp' : datetime.utcnow() + current_app.config['JWT_EXPIRATION_DELTA']}, 
            current_app.config['SECRET_KEY']) 
        return token.decode('UTF-8')
    else:
        print('Invalid user')
        return 0

#Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
  return User.query.get(payload['identity'])

def test_auth(id,psw):
    print('Auth controller test')
    token = authenticate(id,psw)
    return token

