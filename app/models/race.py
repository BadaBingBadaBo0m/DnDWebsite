from db import db, environment, SCHEMA, add_prefix_for_prod

class Race(db.Model):
    __tablename__ = 'races'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    racial_traits = db.Column(db.String(500), nullable=True)
    language = db.Column(db.String(50), nullable=True)
    subrace = db.Column(db.String(50), nullable=True)
    size = db.Column(db.String(50), nullable=True)
    speed = db.Column(db.Integer, nullable=True)