from flask import redirect, render_template, request, session, url_for

from App.models import Cart
from App.models.database import *

def create_cart(customer_id):
    print('create_cart')
    newCart = Cart(customer_id = customer_id)
    db.session.add(newCart)
    db.session.commit()
    print("New cart created for user:",customer_id)
    return newCart

def get_cart(customer_id):
    print('get_cart')
    print('For customer ID: ',customer_id)
    cart = Cart.query.filter_by(customer_id = customer_id, checked_out = False).first()
    return cart.toDict()

def set_checked_out(customer_id):
    print('set_checked_out')
    print('For customer ID: ',customer_id)
    cart = Cart.query.filter_by(customer_id==customer_id, checked_out==False)

    if cart:
        print('Got cart:',cart.toDict())
        cart.checked_out = True
        db.session.commit()
        print('Cart checked out')
        return 1

    print('No cart found')
    return 0