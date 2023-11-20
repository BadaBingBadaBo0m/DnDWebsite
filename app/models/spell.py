from .db import db, environment, SCHEMA, add_prefix_for_prod

class Spell(db.Model):
    __tablename__ = 'spells'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    spell_level = db.Column(db.Integer, nullable=False)
    range = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    effect = db.Column(db.String(500), nullable=False)
    hit_dice = db.Column(db.Integer, nullable=False)
    modifier = db.Column(db.String(100), nullable=False)
    damage_dice = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    saves = db.Column(db.String(100), nullable=True)