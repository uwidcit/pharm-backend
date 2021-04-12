from flask import Blueprint, jsonify

customer_views = Blueprint('customer_views', __name__, template_folder='../templates')

from App.controllers import (
    get_customers
)

@customer_views.route('/customers', methods=["GET"])
def display_customers():
    customerList = get_customers()
    return jsonify(customerList)