from flask import redirect, render_template, request, session, url_for

from App.models import CartItem
from App.models.database import *

def create_cart_item(cart_id, product_id, quantity):
    print('create_cart_item')
    newCartItem = CartItem(cart_id = cart_id, product_id = product_id, quantity = quantity)
    db.session.add(newCartItem)
    db.session.commit()
    print("New item in cart:",cart_id)
    return newCartItem

def delete_cart_item(cart_id, product_id):
    print('delete_cart_item')
    x = CartItem.query.filter_by(cart_id = cart_id, product_id = product_id).delete()
    db.session.commit()
    print("Product {} removed from cart {}".format(product_id,cart_id))
    return x

def get_cart_items(cart_id):
    print('get_cart_items')
    cartItems = CartItem.query.filter_by(cart_id = cart_id).all()

    list_of_items = []
    if cartItems:
        list_of_items = [c.toDict() for c in cartItems]

    return list_of_items
