from app.models import db, Race, environment, SCHEMA
from sqlalchemy.sql import text

def seed_races():
    human = Race(
        name = 'Human',
        description = "Humans are the most adaptable and ambitious people among the common races. Whatever drives them, humans are the innovators, the achievers, and the pioneers of the worlds.",
        racial_traits = '+1 to All Ability Scores, Extra Language',
        size = 'Medium',
        speed = 30
    )

    db.session.add(human)
    db.session.commit()

def undo_races():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.races RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM races"))

    db.session.commit()