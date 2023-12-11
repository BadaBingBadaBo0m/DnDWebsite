from .db import db, environment, SCHEMA, add_prefix_for_prod

class_proficiencies = db.Table(
    'class_proficiencies',
    db.Model.metadata,
    db.Column('class_id', db.Integer, db.ForeignKey(add_prefix_for_prod('classes.id'))),
    db.Column('proficiency_id', db.Integer, db.ForeignKey(add_prefix_for_prod('proficiencies.id')))
)

if environment == 'production':
    class_proficiencies.schema = SCHEMA