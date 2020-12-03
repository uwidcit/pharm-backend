from flask import redirect, render_template, request, session, url_for

from App.models import Product
from App.models.database import *
from App import parse

def create_product(code,name, supplier, supplier_price, qoh, stock, unit_price, total):
    newProd = Product(code = code, product_name = name,  supplier_cost_price = supplier_price, supplier = supplier, QoH = qoh, stock_unit = stock, unit_retail_price = unit_price, total_retail_price = total)
    db.session.add(newProd)
    db.session.commit()
    print("Successfully added")
    return newProd

def parse_excel():
    print('Product controller parse excel')
    prodList = parse.parse()
    print(prodList)

    #--------------------------------------------UNCOMMENT WHEN DB FIXED
    #for p in prodList:
        #print(p[0],p[1],p[2],p[3])
        #x = create_product(p[0],p[1],p[2],p[3])

    return prodList

def get_products():
    print('get_products')
    products = Product.query.all()
    list_of_products = []
    if products:
        list_of_products = [p.toDict() for p in products]
    return list_of_products

def delete_products():
    print('delete_products')
    x = Product.query.delete()
    db.session.commit()
    print('Rows deleted: ',x)
    return 0

def get_all_products():
    list_of_products = []
    products = Product.query.all()
    for product in products:
        list_of_products.append(product.toDict())
    return list_of_products

def get_product_by_name(name):
<<<<<<< HEAD
    product = Product.query.filter_by(name = name).first()
    return product.toDict()
=======
    product = Product.query.filter_by(product_name = name).first()
    return product.toDict()
>>>>>>> 41a0feb25f6d6471b1aeeceb2bb7297794e0e9fa
