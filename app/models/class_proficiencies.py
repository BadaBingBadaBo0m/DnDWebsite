from .db import db, environment, SCHEMA, add_prefix_for_prod

character_proficiencies = db.Table(
    'character_proficiencies',
    db.Model.metadata,
    db.Column('class_id', db.Integer, db.ForeignKey(add_prefix_for_prod('classes.id'))),
    db.Column('proficiency_id', db.Integer, db.ForeignKey(add_prefix_for_prod('proficiencies.id')))
)

if environment == 'production':
    character_proficiencies.schema = SCHEMA