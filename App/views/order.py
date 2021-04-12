from flask import Blueprint, redirect, render_template, request, abort, jsonify
from flask_jwt import jwt_required, current_identity
import json

order_views = Blueprint('order_views', __name__, template_folder='../templates')

from App.controllers import (
    get_user,
    create_order,
    get_orders,
    get_product_by_slug,
    get_users,
    create_order_product,
    get_order_by_id
)

@order_views.route('/create-order', methods=["POST"])
@jwt_required()
def order():
    item_count = request.json.get('item_count')
    order_total = request.json.get('order_total')
    status = request.json.get('status')
    customer = get_user(current_identity.email) #parent
    newOrder = create_order(customer, item_count, order_total, status) #association

    cart = request.json.get('cart') #call get product by slug for list of products
    for product in cart:
        slug = product["slug"]
        #find product by slug and add to list of products
        productObj = get_product_by_slug(slug)
        newOrderProduct = create_order_product(newOrder, productObj)
        newOrder.products.append(newOrderProduct)
    
    return jsonify(newOrder.toDict())

@order_views.route('/orders', methods=["GET"])
def display_orders():
    orderList = get_orders()
    return jsonify(orderList)

@order_views.route('/order', methods=["GET"])
def get_order():
    order_id = request.args.get("id")
    order = get_order_by_id(order_id)
    return jsonify(order.toDict())

@order_views.route('/users', methods=["GET"])
def display_users():
    userList = get_users()
    return jsonify(userList)