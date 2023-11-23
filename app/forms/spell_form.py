from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class SpellForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=1, max=50, message="Character's name must be between 1 to 50 characters!")])
    spell_level = IntegerField('spell_level')
    range = StringField('range', validators=[DataRequired(), Length(min=1, max=50, message="Range must be between 1 to 50 characters!")])
    duration = StringField('duration', validators=[DataRequired(), Length(min=1, max=100, message="Duration must be between 1 to 100 characters!")])
    effect = StringField('effect', validators=[DataRequired(), Length(min=1, max=500, message="Effect must be between 1 to 500 characters!")])
    hit_dice = StringField('hit_dice', validators=[DataRequired(), Length(min=1, max=10, message="Hit dice must be between 1 to 10 characters!")])
    modifier = StringField('modifier', validators=[DataRequired(), Length(min=1, max=100, message="Modifier must be between 1 to 100 characters!")])
    damage_dice = IntegerField('damage_dice')
    description = StringField('description', validators=[Length(min=1, max=500, message="Description must be between 1 to 500 characters!")])
    saves = StringField('saves', validators=[Length(min=1, max=100, message="Saves must be between 1 to 100 characters!")])