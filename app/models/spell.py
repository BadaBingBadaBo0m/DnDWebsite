from .db import db, environment, SCHEMA, add_prefix_for_prod
import datetime

class Spell(db.Model):
    __tablename__ = 'spells'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False, unique=True)
    range = db.Column(db.String(255), nullable=False, )
    duration = db.Column(db.String(255), nullable=False, )
    components = db.Column(db.String(255), nullable=False)
    ritual = db.Column(db.Boolean, nullable=False)
    concentration = db.Column(db.Boolean, nullable=False)
    casting_time = db.Column(db.String(255), nullable=False)
    damage_at_slot_level = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'range': self.range,
            'duration': self.duration,
            'components': self.components,
            'ritual': self.ritual,
            'concentration': self.concentration,
            'casting_time': self.casting_time,
            'damage_at_slot_level': self.damage_at_slot_level
        }
