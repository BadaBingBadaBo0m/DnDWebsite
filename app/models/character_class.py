from .db import db, environment, SCHEMA, add_prefix_for_prod

class Character_Class(db.Model):
    __tablename__ = 'classes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    hit_points = db.Column(db.Integer, nullable=False)
    hit_dice = db.Column(db.String(50), nullable=False)
    hit_point_modifier = db.Column(db.String(50), nullable=False)

    # Class and characters relationship
    characters = db.relationship('Character', secondary='character_classes', back_populates='classes')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'hit_points': self.hit_points,
            'hit_dice': self.hit_dice,
            'hit_point_modifier': self.hit_point_modifier
        }