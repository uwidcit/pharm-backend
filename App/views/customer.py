from flask import Blueprint, jsonify, request

customer_views = Blueprint('customer_views', __name__, template_folder='../templates')

from App.controllers import (
    get_customers,
    delete_customer_by_id,
)

@customer_views.route('/customers', methods=["GET"])
def display_customers():
    customerList = get_customers()
    return jsonify(customerList)

@customer_views.route('/delete-customer', methods=["GET"])
def delete_customer():
    customer_id = request.args.get("id")
    deleted = delete_customer_by_id(customer_id)
    return jsonify({"deleted" : deleted})