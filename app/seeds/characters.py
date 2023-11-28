from app.models import db, Character, environment, SCHEMA
from sqlalchemy.sql import text

def seed_characters():
    character1 = Character(
        owner_id = 1,
        level = 1,
        name = "Bruh",
        gender = "Male",
        race_id = 1,
        description = "I am a cool guy",
        hit_points = 10,
        strength = 10,
        dexterity = 10,
        constitution = 10,
        intelligence = 10,
        wisdom = 10,
        charisma = 10
    )

    character2 = Character(
        owner_id = 1,
        level = 1,
        name = "Bruhasdfasdf",
        gender = "Male",
        race_id = 2,
        description = "I am a cool guy",
        hit_points = 10,
        strength = 10,
        dexterity = 10,
        constitution = 10,
        intelligence = 10,
        wisdom = 10,
        charisma = 10
    )

    character3 = Character(
        owner_id = 1,
        level = 1,
        name = "Bartholomew",
        gender = "Male",
        race_id = 1,
        description = "I am not a cool guy",
        hit_points = 10,
        strength = 10,
        dexterity = 10,
        constitution = 10,
        intelligence = 10,
        wisdom = 10,
        charisma = 10
    )

    db.session.add(character1)
    db.session.add(character2)
    db.session.add(character3)

    db.session.commit()

def undo_characters():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.characters RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM characters"))

    db.session.commit()