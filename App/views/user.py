from flask import Blueprint, redirect, render_template, request, jsonify
import json

user_views = Blueprint('user_views', __name__, template_folder='../templates')

from App.controllers import (
    get_profile
)

@user_views.route('/profile/', methods=["GET"])
def display_profile():
    print('display_profile view')

    searchTerm = request.args.get('search')
    if(searchTerm):
        profile = get_profile(searchTerm)
    else:
        profile = "User not found"
    return jsonify(profile)