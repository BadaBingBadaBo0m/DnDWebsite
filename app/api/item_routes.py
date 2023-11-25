from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Item, db 
from .auth_routes import validation_errors_to_error_messages
#from app.forms import SpellForm
from datetime import datetime

item_routes = Blueprint('items', __name__)


#Query for all items and returns them in a list of dictionaries
@item_routes.route('/')
def items():
    """
    Query for all items and returns them in a list of item dictionaries
    """
    items= Item.query.all()
    return_list = []
    for item in items:
        item_dict = item.to_dict()
        return_list.append(item_dict)
    return return_list

# Query for one item and returns in a dictionary
@item_routes.route('/<id>')
def item(id):
    """
    Query for one item and returns it in a dictionary
    """
    item = Item.query.get(id)

    if not item:
        return {'Errors': ['Item does not exist!']}, 404

    return item.to_dict()
