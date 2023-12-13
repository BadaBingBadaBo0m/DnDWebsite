from .db import db, environment, SCHEMA, add_prefix_for_prod
import datetime

class Ability_Score(db.Model):
    __tablename__ = 'ability_scores'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False, unique=True)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
