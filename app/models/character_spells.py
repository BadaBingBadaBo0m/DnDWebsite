from .db import db, environment, SCHEMA, add_prefix_for_prod

character_spells = db.Table(
    'character_spells',
    db.Model.metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('character_id', db.Integer, db.ForeignKey(add_prefix_for_prod('characters.id'))),
    db.Column('spell_id', db.Integer, db.ForeignKey(add_prefix_for_prod('spells.id')))
)

if environment == "production":
    character_spells.schema = SCHEMA