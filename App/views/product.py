from flask import Blueprint, redirect, render_template, request, jsonify
import json

product_views = Blueprint('product_views', __name__, template_folder='../templates')

from App.controllers import (
    get_products
)

@product_views.route('/products', methods=["GET"])
def display_event():
    prodList = get_products()
    return jsonify(prodList)
    #return json.dumps(prodList)