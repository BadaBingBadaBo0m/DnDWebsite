from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Character, db 
from .auth_routes import validation_errors_to_error_messages
from app.forms import CharacterForm
from datetime import date

character_routes = Blueprint('characters', __name__)

@character_routes.route('/<id>')
def character(id):
    """
    Query for one character and returns it in a dictionary
    """
    character = Character.query.get(id)
    return character.to_dict()


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


@character_routes.route('/delete/<id>', methods=['DELETE'])
@login_required
def deleta_a_character(id):
    """
    Query for deleting a character
    """
    current_user_dict = current_user.to_dict()
    to_delete = Character.query.get(id)
    
    if not to_delete:
        return {'Message': 'Character does not exist'}
    
    to_delete_dict = to_delete.to_dict()

    if current_user_dict['id'] == to_delete_dict['owner_id']:
        db.session.delete(to_delete)
        db.session.commit()
        return {'Message': 'Character deleted'}
    return {'Message': 'You do not have permission to delete this character'}