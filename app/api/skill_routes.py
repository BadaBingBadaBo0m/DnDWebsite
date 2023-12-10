from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Skill, db 
from .auth_routes import validation_errors_to_error_messages
# TODO ADD FORMS
#from app.forms import SpellForm
from datetime import datetime

skill_routes = Blueprint('skills', __name__)


#Query for all skills and returns them in a list of dictionaries
@skill_routes.route('/')
def skills():
    """
    Query for all skills and returns them in a list of dictionaries
    """
    skills= Skill.query.all()
    return_list = []
    for skill in skills:
        skill_dict = skill.to_dict()
        return_list.append(skill_dict)
    return return_list

# Query for one skill and returns in a skill dictionary
@skill_routes.route('/<id>')
def skill(id):
    """
    Query for one skill and returns it in a dictionary
    """
    skill = Skill.query.get(id)

    if not skill:
        return {'Errors': ['Skill does not exist!']}, 404

    return skill.to_dict()
