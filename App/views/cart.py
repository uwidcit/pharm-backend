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
@cart_views.route('/cart', methods=['POST'])
def cart():
    print('cart view')
    
    cartJson = request.json
    if cartJson:
        print('Cart json:',cartJson)

        cart = cartJson['cart_id']
        print('Cart:',cart)

        product = cartJson['product_id']
        print('Product:',product)

        quantity = cartJson['quantity']
        print('Quantity:',quantity)

        if cart and product and quantity:
            print('Adding items to cart')
            cartItem = create_cart_item(cart,product,quantity)

        cartList = get_cart_items(cart)
        return jsonify(cartList)
    else:
        return 400