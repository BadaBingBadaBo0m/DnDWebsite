from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Character, db 
from .auth_routes import validation_errors_to_error_messages
from app.forms import character_form
from datetime import date

character_routes = Blueprint('characters', __name__)

@character_routes.route('/<id>')
def character(id):
    """
    Query for one character and returns it in a dictionary
    """
    character = Character.query.get(id)
    return character.to_dict()