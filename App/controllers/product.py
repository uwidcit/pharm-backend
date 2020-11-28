from flask import redirect, render_template, request, session, url_for

from App.models import Product
from App.models.database import *

def create_product(name, desc, img, price):
    newProd = Product(name = name, description = desc, image = img, unit_price = price)
    db.session.add(newProd)
    db.session.commit()
    print("Successfully added")
    return newProd

def get_all_products():
    list_of_products = []
    products = Product.query.all()
    for product in products:
        list_of_products.append(product.toDict())
    return list_of_products

def get_product_by_name(name):
    product = Product.query.filter_by(name = name).first()
    return product.toDict()