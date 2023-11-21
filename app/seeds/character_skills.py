from app.models import db, environment, SCHEMA
from sqlalchemy.sql import text
from app.models.character_skills import character_skills

def seed_character_skills():
    connection = db.engine.connect()

    data = [
        {"character_id": 1, "skill_id": 1, "bonus": 1}
    ]

    for spell in data:
        connection.execute(character_spells.insert(), spell)

    connection.close()

def undo_character_skills():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.character_skills RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM character_skills"))

    db.session.commit()