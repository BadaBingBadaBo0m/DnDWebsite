from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Spell, db 
from .auth_routes import validation_errors_to_error_messages
from app.forms import SpellForm
from datetime import datetime

spell_routes = Blueprint('spells', __name__)


#Query for all spells and returns them in a spell dictionary
@spell_routes.route('/')
def spells():
    """
    Query for all characters and returns them in a list of spell dictionaries
    """
    spells= Spell.query.all()
    return_list = []
    for spell in spells:
        spell_dict = spell.to_dict()
        return_list.append(spell_dict)
    return return_list

# Query for one spell and returns in in a spell dictionary
@spell_routes.route('/<id>')
def spell(id):
    """
    Query for one spell and returns it in a dictionary
    """
    spell = Spell.query.get(id)

    if not spell:
        return {'Errors': ['Spell does not exist!']}, 404

    return spell.to_dict()
