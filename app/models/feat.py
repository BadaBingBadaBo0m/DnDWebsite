from .db import db, environment, SCHEMA, add_prefix_for_prod

class Feat(db.Model):
    __tablename__ = 'feats'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    characters = db.relationship('Character', secondary='character_feats', back_populates='feats')