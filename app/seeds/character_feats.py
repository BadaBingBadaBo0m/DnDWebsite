from app.models import db, environment, SCHEMA
from sqlalchemy.sql import text
from app.models.character_feats import character_feats

def seed_character_feats():
    connection = db.engine.connect()

    data = [
        {"character_id": 1, "feat_id": 1, "bonus": 1}
    ]

    for feat in data:
        connection.execute(character_feats.insert(), feat)

    connection.close()

def undo_character_feats():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.character_feats RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM character_feats"))

    db.session.commit()