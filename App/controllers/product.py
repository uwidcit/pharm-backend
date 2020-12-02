from flask import redirect, render_template, request, session, url_for

from App.models import Product
from App.models.database import *

def create_product(code,name, supplier, supplier_price, qoh, stock, unit_price, total):
    newProd = Product(code = code, product_name = name,  supplier_cost_price = supplier_price, supplier = supplier, QoH = qoh, stock_unit = stock, unit_retail_price = unit_price, total_retail_price = total)
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
    product = Product.query.filter_by(product_name = name).first()
    return product.toDict()