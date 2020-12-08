from flask import Blueprint, redirect, render_template, request, jsonify
import json

cart_views = Blueprint('cart_views', __name__, template_folder='../templates')

from App.controllers import (
    create_cart_item,
    get_cart_items
)

#Requires a cart to already be created in the DB
#You can do so by using the createCart function in the manage script
#I created cart with ID 2 already for the demo
@cart_views.route('/cart/', methods=['GET', 'POST'])
def cart():
    print('cart view')

    cart = request.args.get('cart')
    if cart is None:
        cart = 2
    print('Cart:',cart)

    product = request.args.get('product')
    print('Product:',product)

    quantity = request.args.get('quantity')
    print('Quantity:',quantity)

    cartItem = create_cart_item(cart,product,quantity)
    cart = get_cart_items(cart)
    return jsonify(cart)