from flask import redirect, render_template, request, session, url_for

from App.models import Product
from App.models.database import *
from App import parsecsv

def create_product(name, desc, img, price):
    newProd = Product(name = name, description = desc, image = img, unit_price = price)
    db.session.add(newProd)
    db.session.commit()
    print("Successfully added")
    return newProd

def parse_csv():
    print('Product controller parse csv')
    prodList = parsecsv.parse()
    #print(prodList)
    for p in prodList:
        #print(p[0],p[1],p[2],p[3])
        x = create_product(p[0],p[1],p[2],p[3])
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