from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Character_Class, db 
from .auth_routes import validation_errors_to_error_messages
#from app.forms import SpellForm
from datetime import datetime

character_class_routes = Blueprint('classes', __name__)


#Query for all classes and returns them in a list of dictionaries
@character_class_routes.route('/')
def classes():
    """
    Query for all classes and returns them in a list of class dictionaries
    """
    classes= Character_Class.query.all()
    return_list = []
    for character_class in classes:
        class_dict = character_class.to_dict()
        return_list.append(class_dict)
    return return_list

# Query for one class and returns in a dictionary
@character_class_routes.route('/<id>')
def character_class(id):
    """
    Query for one class and returns it in a dictionary
    """
    character_class = Character_Class.query.get(id)

    if not character_class:
        return {'Errors': ['Class does not exist!']}, 404

    return character_class.to_dict()