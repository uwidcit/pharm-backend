from flask import redirect, render_template, request, session, url_for

from App.models import ( Order )
from App.models.database import db

def create_order(customer, item_count, order_total, status):
    newOrder = Order(user_id = customer.id, item_count = item_count, order_total = order_total, pickup_status = status)
    print("Successfully Created")
    db.session.add(newOrder)
    db.session.commit()
    return newOrder

def get_orders():
    print('get all orders')
    orders = Order.query.all()
    list_of_orders = []
    if orders:
        list_of_orders = [o.toDict() for o in orders]
    return list_of_orders

def get_order_by_id(order_id):
    print("getting order")
    order = Order.query.filter(Order.id == order_id).first() 
    return order

def get_orders_by_term(term):
    list_of_orders = []
    orders = Order.query.filter(
        Order.id.contains(term)
        | Order.pickup_status.contains(term)
        | Order.user.has(email = term)
        | Order.user.has(first_name = term)
        | Order.user.has(last_name = term)
        | Order.order_total.contains(term)
        | Order.date_placed.contains(term)
    )
    if orders:
        list_of_orders = [o.toDict() for o in orders]
    return list_of_orders