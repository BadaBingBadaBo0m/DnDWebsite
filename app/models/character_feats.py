from .db import db, environment, SCHEMA, add_prefix_for_prod

character_feats = db.Table(
    'character_feats',
    db.Model.metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('character_id', db.Integer, db.ForeignKey(add_prefix_for_prod('characters.id'))),
    db.Column('feat_id', db.Integer, db.ForeignKey(add_prefix_for_prod('feats.id'))),
    db.Column('bonus', db.Integer,)
)

if environment == "production":
    character_feats.schema = SCHEMA