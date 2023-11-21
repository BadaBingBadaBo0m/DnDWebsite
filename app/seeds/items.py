from app.models import db, Item, environment, SCHEMA
from sqlalchemy.sql import text

def seed_items():
    item1 = Item(
        name = "Longsword",
        description = "Proficiency with a longsword allows you to add your proficiency bonus to the attack roll for any attack you make with it.",
        type = "Weapon",
        damage = "1d8 slashing",
        weight = 3.2,
        cost = 15
    )

    db.session.add(item1)
    db.session.commit()

def undo_items():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM items"))

    db.session.commit()