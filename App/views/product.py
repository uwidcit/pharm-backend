from flask import Blueprint, request, jsonify

product_views = Blueprint('product_views', __name__, template_folder='../templates')

from App.controllers import (
    get_products_page,
    get_page_details,
    get_product_categories,
    get_product_by_slug,
    delete_product_by_slug
)

@product_views.route('/products', methods=["GET"])
def display_event():
    page = request.args.get('page')
    prodList = get_products_page(page)
    return jsonify(prodList)

@product_views.route('/products_page', methods=["GET"])
def display_pages():
    page = request.args.get('page')
    pageList = get_page_details(page)
    return jsonify(pageList)

@product_views.route('/product_categories', methods=["GET"])
def display_categories():
    categoryList = get_product_categories()
    return jsonify(categoryList)

@product_views.route('/product', methods=["GET"])
def get_product():
    product_slug = request.args.get("slug")
    product = get_product_by_slug(product_slug)
    return jsonify(product.toDict())

@product_views.route('/create-product', methods=["POST"])
def create_product():
    code = request.json.get("code")
    name = request.json.get("name")
    category = request.json.get("category")
    supplier_cost_price = request.json.get("supplier_cost_price")
    supplier = request.json.get("supplier")
    QoH = request.json.get("QoH")
    stock_unit = request.json.get("stock_unit")
    unit_retail_price = request.json.get("unit_retail_price")
    total_retail_price = request.json.get("total_retail_price")
    image = request.json.get("image")
    

@product_views.route('/delete-product', methods=["DELETE"])
def delete_product():
    product_slug = request.args.get("slug")
    deleted = delete_product_by_slug(product_slug)
    return jsonify({"deleted": deleted})