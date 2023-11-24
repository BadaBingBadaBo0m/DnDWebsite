from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Feat, db 
from .auth_routes import validation_errors_to_error_messages
#from app.forms import SpellForm
from datetime import datetime

feat_routes = Blueprint('feats', __name__)


#Query for all feats and returns them in a feat dictionary
@feat_routes.route('/')
def feats():
    """
    Query for all feats and returns them in a list of feat dictionaries
    """
    feats= Feat.query.all()
    return_list = []
    for feat in feats:
        feat_dict = feat.to_dict()
        return_list.append(feat_dict)
    return return_list

# Query for one feat and returns in a feat dictionary
@feat_routes.route('/<id>')
def feat(id):
    """
    Query for one feat and returns it in a dictionary
    """
    feat = Feat.query.get(id)

    if not feat:
        return {'Errors': ['Feat does not exist!']}, 404

    return feat.to_dict()