from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Character, db 
from .auth_routes import validation_errors_to_error_messages
from app.forms import CharacterForm
from datetime import datetime

character_routes = Blueprint('characters', __name__)


# Query for one character and returns in a character dictionary
@character_routes.route('/<id>')
def character(id):
    """
    Query for one character and returns it in a dictionary
    """
    character = Character.query.get(id)

    if not character:
        return {'Errors': ['Character does not exist!']}, 404

    return character.to_dict()


# Create a character and returns it in a character dictionary
@character_routes.route('/create', methods=['POST'])
@login_required
def create_a_character():
    """
    Query for creating a character and returning it in a dictionary
    """
    form = CharacterForm()
    current_user_dict = current_user.to_dict()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_character = Character(
            owner_id=current_user_dict['id'],
            level=1,
            name=form.data['name'],
            gender=form.data['gender'],
            description=form.data['description'],
            hit_points=form.data['hit_points'],
            strength=form.data['strength'],
            dexterity=form.data['dexterity'],
            constitution=form.data['constitution'],
            intelligence=form.data['intelligence'],
            wisdom=form.data['wisdom'],
            charisma=form.data['charisma'],
            race_id=form.data['race_id']
        )
        db.session.add(new_character)
        db.session.commit()
        return new_character.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@character_routes.route('/edit/<id>', methods=['PUT'])
@login_required
def edit_a_character(id):
    """
    Query for editing an existing character the current user has created
    """
    form = CharacterForm()
    current_user_dict = current_user.to_dict()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        character_to_edit = Character.query.get(id)

        if not character_to_edit:
            return {'Errors': ['Character does not exist!']}, 404

        character_to_edit_dict = character_to_edit.to_dict()

        if character_to_edit_dict['owner_id'] == current_user_dict['id']:
            character_to_edit.level = form.data['level']
            character_to_edit.name = form.data['name']
            character_to_edit.gender = form.data['gender']
            character_to_edit.description = form.data['description']
            character_to_edit.hit_points = form.data['hit_points']
            character_to_edit.strength = form.data['strength']
            character_to_edit.dexterity = form.data['dexterity']
            character_to_edit.constitution = form.data['constitution']
            character_to_edit.intelligence = form.data['intelligence']
            character_to_edit.wisdom = form.data['wisdom']
            character_to_edit.charisma = form.data['charisma']
            character_to_edit.race_id = form.data['race_id']
            character_to_edit.updatedAt = datetime.now()
            db.session.commit()
            returning_value = character_to_edit.to_dict()
            return returning_value
        return {'Errors': ['You do not have permission to edit this character!']}, 403
    return {'errors': validation_errors_to_error_messages(form.errors)},401

# Delete a character and returns a message
@character_routes.route('/delete/<id>', methods=['DELETE'])
@login_required
def deleta_a_character(id):
    """
    Query for deleting a character
    """
    current_user_dict = current_user.to_dict()
    to_delete = Character.query.get(id)
    
    if not to_delete:
        return {'Errors': ['Character does not exist!']}, 404
    
    to_delete_dict = to_delete.to_dict()

    if current_user_dict['id'] == to_delete_dict['owner_id']:
        db.session.delete(to_delete)
        db.session.commit()
        return {'Message': 'Character deleted'}
    return {'Errors': ['You do not have permission to delete this character!']}, 403