from flask import redirect, render_template, request, session, url_for

from App.models import Product
from App.models.database import *

def create_product(name, desc, img, price):
    newProd = Product(name = name, description = desc, image = img, unit_price = price)
    db.session.add(newProd)
    db.session.commit()
    print("Successfully added")
    return newProd