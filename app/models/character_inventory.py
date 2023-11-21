from .db import db, environment, SCHEMA, add_prefix_for_prod

character_inventory = db.Table(
    'character_inventory',
    db.Model.metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('character_id', db.Integer, db.ForeignKey(add_prefix_for_prod('characters.id'))),
    db.Column('item_id', db.Integer, db.ForeignKey(add_prefix_for_prod('items.id'))),
    db.Column('quantity', db.String(10), nullable=False),
    db.Column('equipped', db.Boolean, nullable=False)
)

if environment == "production":
    character_inventory.schema = SCHEMA