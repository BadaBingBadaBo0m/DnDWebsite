from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Campaign(db.Model):
    __tablename__ = 'campaigns'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    # User and campaign relationship
    owner = db.relationship('User', back_populates='campaigns')
    # Character and campaign relationship
    characters = db.relationship('Character', secondary='campaign_characters', back_populates='campaign')

    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'owner': self.owner.to_dict(),
            'characters': [character.to_dict() for character in self.characters]
        }
    
    def to_dict_simple(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'name': self.name,
            'description': self.description,
        }