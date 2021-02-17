from flask import redirect, render_template, request, session, url_for

from App.models import Product
from App.models.database import db
from App import parse

def create_product(code, name, category, supplier_price, supplier, qoh, stock, unit_price, total):
    newProd = Product(code = code, product_name = name, category = category, supplier_cost_price = supplier_price, supplier = supplier, QoH = qoh, stock_unit = stock, unit_retail_price = unit_price, total_retail_price = total)
    db.session.add(newProd)
    db.session.commit()
    #print("Successfully added")
    return newProd

def parse_excel():
    print('Product controller parse excel')
    prodList = parse.parse()
    #print(prodList)

    print('Inserting products in DB (This may take several minutes).....')
    if prodList:
        for p in prodList:
            #print('Code: {}\nProduct Name: {}\nCategory: {}\nSupplier Cost Price: {}\nSupplier: {}\nQoH: {}\nStock Unit: {}\nUnit Retail: {}\nTotal Retail Price: {}\n'
            #.format(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]))

            x = create_product(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])
        print('Finished!')
        return 1
    else:
        print('No products parsed')
        return 0

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
    
def get_product_by_name(name):
    product = Product.query.filter_by(product_name = name).first()
    return product.toDict()
