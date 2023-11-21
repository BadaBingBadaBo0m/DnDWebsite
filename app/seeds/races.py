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

    tiefling = Race(
        name = 'Tiefling',
        description = "To be greeted with stares and whispers, to suffer violence and insult on the street, to see mistrust and fear in every eye: this is the lot of the tiefling.",
        racial_traits = '+2 Charisma, +1 Intelligence, Darkvision, Hellish Resistance, Infernal Legacy',
        size = 'Medium',
        speed = 30
    )

    db.session.add(human)
    db.session.add(tiefling)
    db.session.commit()

def undo_races():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.races RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM races"))

    db.session.commit()