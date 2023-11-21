from app.models import db, Feat, environment, SCHEMA
from sqlalchemy.sql import text

def seed_feats():
    feat1 = Feat(
        name = 'Charger',
        description = "	As part of the Dash action you can make a melee attack with a +5 bonus if you move at least 10 ft before."
    )

    db.session.add(feat1)
    db.session.commit()

def undo_feats():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.feats RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM feats"))

    db.session.commit()