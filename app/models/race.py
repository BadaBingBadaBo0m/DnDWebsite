from .db import db, environment, SCHEMA, add_prefix_for_prod

class Race(db.Model):
    __tablename__ = 'races'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    size_description = db.Column(db.String(500), nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    alignment = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "size": self.size,
            "size_description": self.size_description,
            "speed": self.speed,
            "alignment": self.alignment
        }