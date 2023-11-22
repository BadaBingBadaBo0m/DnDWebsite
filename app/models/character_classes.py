from .db import db, environment, SCHEMA, add_prefix_for_prod

character_classes = db.Table(
    'character_classes',
    db.Model.metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('class_id', db.Integer, db.ForeignKey(add_prefix_for_prod('classes.id'))),
    db.Column('character_id', db.Integer, db.ForeignKey(add_prefix_for_prod('characters.id')))
)

if environment == "production":
    character_classes.schema = SCHEMA