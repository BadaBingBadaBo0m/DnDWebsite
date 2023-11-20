from app.models import db, environment, SCHEMA
from sqlalchemy.sql import text
from app.models.character_spells import character_spells

def seed_character_spells():
    connection = db.engine.connect()

    data = [
        {"character_id": 1, "spell_id": 1}
    ]

    for spell in data:
        connection.execute(character_spells.insert(), spell)

    connection.close()

def undo_channel_members():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.character_spells RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM character_spells"))

    db.session.commit()