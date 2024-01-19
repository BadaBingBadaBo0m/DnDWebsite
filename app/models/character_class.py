from .db import db, environment, SCHEMA, add_prefix_for_prod

class Character_Class(db.Model):
    __tablename__ = 'classes'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    hit_die = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    max_skill_proficiencies = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)

    # proficiencies = db.relationship("Proficiency", secondary="class_proficiencies", back_populates="classes")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "hit_die": self.hit_die,
            "description": self.description,
            "max_skill_proficiencies": self.max_skill_proficiencies,
            "level": self.level
        }