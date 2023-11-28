from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Character(db.Model):
    __tablename__ = 'characters'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
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
    race_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('races.id')), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    # User and character relationship
    owner = db.relationship('User', back_populates='characters')
    # Character and spell relationship
    spells = db.relationship('Spell', secondary='character_spells', back_populates='characters')
    # Character and skill relationship
    skills = db.relationship('Skill', secondary='character_skills', back_populates='characters')
    # Character and race relationship
    race = db.relationship('Race', back_populates='characters')
    # Character and feat relationship
    feats = db.relationship('Feat', secondary='character_feats', back_populates='characters')
    # Character and inventory relationship
    items = db.relationship('Item', secondary='character_inventories', back_populates='characters')
    # Character and campaign relationship
    campaign = db.relationship('Campaign', secondary='campaign_characters', back_populates='characters')
    # Character and class relationship
    classes = db.relationship('Character_Class', secondary='character_classes', back_populates='characters')

    def user_character_to_dict(self):
        return {
            'id': self.id,
            'level': self.level,
            'name': self.name,
            'campaigns': [campaign.to_dict_simple() for campaign in self.campaign],
            'classes': [class_.to_dict() for class_ in self.classes],
            'race': self.race.to_dict()
        }

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
            'owner_id': self.owner_id,
            'race_id': self.race_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'owner': self.owner.to_dict(),
            'spells': [spell.to_dict() for spell in self.spells],
            'skills': [skill.to_dict() for skill in self.skills],
            'items': [item.to_dict() for item in self.items],
            'campaigns': [campaign.to_dict_simple() for campaign in self.campaign],
            'classes': [class_.to_dict() for class_ in self.classes],
            'race': self.race.to_dict()
        }