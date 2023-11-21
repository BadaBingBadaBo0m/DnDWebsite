from app.models import db, Campaign, environment, SCHEMA
from sqlalchemy.sql import text

def seed_campaigns():
    campaign1 = Campaign(
        owner_id = 2,
        name = 'The Lost Mine of Phandelver',
        description = "A Dungeons & Dragons 5th Edition adventure for 1st level characters, the Lost Mine of Phandelver is the introductory adventure in the Dungeons & Dragons 5th Edition Starter Set. It is designed for a party of 4-5 players, with levels 1-5."
    )

    db.session.add(campaign1)
    db.session.commit()

def undo_campaigns():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.campaigns RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM campaigns"))

    db.session.commit()