from app.models import db, Spell, environment, SCHEMA
from sqlalchemy.sql import text

def seed_spells():
    spell1 = Spell(
        name = "Fireball",
        spell_level = 1,
        range = "120 ft",
        duration = "Instantaneous",
        effect = "fire",
        hit_dice = "1d20",
        description = "You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn't being worn or carried.",
        modifier = "gfgd",
        damage_dice = 4,
        saves = 10
    )

    db.session.add(spell1)
    db.session.commit()

def undo_spells():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.spells RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM spells"))

    db.session.commit()