from .db import db, environment, SCHEMA, add_prefix_for_prod

character_skills = db.Table(
    'character_skills',
    db.Model.metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('character_id', db.Integer, db.ForeignKey(add_prefix_for_prod('characters.id'))),
    db.Column('skill_id', db.Integer, db.ForeignKey(add_prefix_for_prod('skills.id'))),
    db.Column('bonus', db.Integer,)
)

if environment == "production":
    character_skills.schema = SCHEMA