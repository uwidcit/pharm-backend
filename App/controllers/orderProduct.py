from flask import redirect, render_template, request, session, url_for

from App.models import ( OrderProduct )
from App.models.database import db

def create_order_product(order, product):
    newOrderProduct = OrderProduct(order_id = order.id, product_id = product.id)
    print("Successfully Created")
    db.session.add(newOrderProduct)
    db.session.commit()
    return newOrderProduct
