from app.models import db, Spell, environment, SCHEMA
from sqlalchemy import text

def seed_spells():
    fireball = Spell(
        name = "Fireball",
        description = "You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn't being worn or carried.",
        range = "150 feet",
        duration = "Instantaneous",
        components = "V, S, M",
        ritual = False,
        concentration = False,
        casting_time = "1 action",
        damage_at_slot_level = "8d6, 9d6, 10d6, 11d6, 12d6, 13d6, 14d6"
    )

    db.session.add(fireball)
    
    db.session.commit()

def undo_spells():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.spells RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM spells"))

    db.session.commit()