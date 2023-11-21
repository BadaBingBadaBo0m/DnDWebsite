from app.models import db, environment, SCHEMA
from sqlalchemy.sql import text
from app.models.campaign_characters import campaign_characters

def seed_campaign_characters():
    connection = db.engine.connect()

    data = [
        {"campaign_id": 1, "character_id": 1}
    ]

    for character in data:
        connection.execute(campaign_characters.insert(), character)

    connection.close()

def undo_campaign_characters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.campaign_characters RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM campaign_characters"))

    db.session.commit()