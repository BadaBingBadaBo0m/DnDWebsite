from app.models import db, environment, SCHEMA
from sqlalchemy.sql import text
from app.models.character_classes import character_classes

def seed_character_classes():
    connection = db.engine.connect()

    data = [
        {"class_id": 1, "character_id": 1}
    ]

    for character in data:
        connection.execute(character_classes.insert(), character)

    connection.close()

def undo_character_classes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.character_classes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM character_classes"))

    db.session.commit()