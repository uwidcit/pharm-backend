from flask import Blueprint, redirect, render_template, request, jsonify
import json

product_views = Blueprint('product_views', __name__, template_folder='../templates')

from App.controllers import (
    get_products
)

@product_views.route('/products/', methods=["GET"])
def display_products():
    print('display_products view')

    search = request.args.get('search')
    #print('Search:',search)

    limit = request.args.get('limit')
    #print('Limit:',limit)

    offset = request.args.get('offset')
    #print('Offset:',offset)

    print('Getting all products')
    prodList = get_products(search,limit,offset)
    return jsonify(prodList)
    #return json.dumps(prodList)