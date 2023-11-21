from .db import db, environment, SCHEMA, add_prefix_for_prod

class Item(db.Model):
    __tablename__ = 'items'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    damage = db.Column(db.String(100), nullable=True)
    weight = db.Column(db.Float, nullable=False)
    cost = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'type': self.type,
            'damage': self.damage,
            'weight': self.weight,
            'cost': self.cost 
        }