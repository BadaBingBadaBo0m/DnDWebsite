from app.models import db, environment, SCHEMA
from sqlalchemy.sql import text
from app.models.character_inventories import character_inventories

def seed_character_inventories():
    connection = db.engine.connect()

    data = [
        {"character_id": 1, "item_id": 1, "quantity": "1", "equipped": True},
    ]

    for inventory in data:
        connection.execute(character_inventories.insert(), inventory)

    connection.close()

def undo_character_inventories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.character_inventories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM character_inventories"))

    db.session.commit()