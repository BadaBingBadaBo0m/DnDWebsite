from .db import db, environment, SCHEMA, add_prefix_for_prod
import datetime

class Character(db.Model):
    __tablename__ = 'characters'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    gender = db.Column(db.String(255), nullable=False, unique=True)
    descripton = db.Column(db.String(255), nullable=False, unique=True)
    createdAt = db.Column(db.DateTime, default=db.func.now())
    updatedAt = db.Column(db.DateTime, default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
