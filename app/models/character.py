from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Character(db.Model):
    __tablename__ = 'characters'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('users.id')), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    hit_points = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    constitution = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    wisdom = db.Column(db.Integer, nullable=False)
    charisma = db.Column(db.Integer, nullable=False)
    #skills = db.Column(db.String(50), nullable=True)
    #spell_slot = db.Column(db.String(50), nullable=True)
    #race = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    # User and character relationship
    owner = db.relationship('User', back_populates='characters')

    def to_dict(self):
        return {
            'id': self.id,
            # 'owner_id': self.owner_id,
            'level': self.level,
            'name': self.name,
            'gender': self.gender,
            'description': self.description,
            'hit_points': self.hit_points,
            'strength': self.strength,
            'dexterity': self.dexterity,
            'constitution': self.constitution,
            'intelligence': self.intelligence,
            'wisdom': self.wisdom,
            'charisma': self.charisma,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'owner': self.owner.to_dict()
        }