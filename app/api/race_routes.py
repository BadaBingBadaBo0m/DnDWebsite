from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Race, db 
from .auth_routes import validation_errors_to_error_messages
# TODO ADD FORMS
#from app.forms import SpellForm
from datetime import datetime

race_routes = Blueprint('races', __name__)


#Query for all races and returns them in a list of dictionaries
@race_routes.route('/')
def races():
    """
    Query for all races and returns them in a list of dictionaries
    """
    races= Race.query.all()
    return_list = []
    for race in races:
        race_dict = race.to_dict()
        return_list.append(race_dict)
    return return_list

# Query for one race and returns in a dictionary
@race_routes.route('/<id>')
def race(id):
    """
    Query for one race and returns it in a dictionary
    """
    race = Race.query.get(id)

    if not race:
        return {'Errors': ['Race does not exist!']}, 404

    return race.to_dict()
