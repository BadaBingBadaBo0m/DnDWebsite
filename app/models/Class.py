from .db import db, environment, SCHEMA, add_prefix_for_prod

class Class(db.Model):
    __tablename__ = 'classes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    hit_points = db.Column(db.Integer, nullable=False)
    hit_dice = db.Column(db.String(50), nullable=False)
    hit_point_modifier = db.Column(db.String(50), nullable=False)