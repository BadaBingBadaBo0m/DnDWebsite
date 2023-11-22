from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class CharacterForm(FlaskForm):
    owner_id = IntegerField('owner')
    level = IntegerField('level')
    name = StringField('name', validators=[DataRequired(), Length(min=1, max=50, message="Character's name must be between 1 to 50 characters!")])
    gender = StringField('gender', validators=[DataRequired(), Length(min=1, max=50, message="Character's gender must be between 1 to 50 characters!")])
    description = StringField('description', validators=[DataRequired(), Length(min=1, max=500, message="Character's description must be between 1 to 500 characters!")])
    hit_points = IntegerField('hit_points')
    strength = IntegerField('strength')
    dexterity = IntegerField('dexterity')
    constitution = IntegerField('constitution')
    intelligence = IntegerField('intelligence')
    wisdom = IntegerField('wisdom')
    charisma = IntegerField('charisma')
    race_id = IntegerField("race_id")