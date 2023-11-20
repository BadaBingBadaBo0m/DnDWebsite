from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Character(db.Model):
    __tablename__ = 'characters'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    # User id foreign key (should we change this to owner id?)
    name = db.Column(db.String(50), nullable=False)
    race = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    hit_points = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    constitution = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    wisdom = db.Column(db.Integer, nullable=False)
    charisma = db.Column(db.Integer, nullable=False)
    skills = db.Column(db.String(50), nullable=True)
    spell_slot = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())