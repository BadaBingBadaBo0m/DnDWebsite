from app.models import db, Spell, environment, SCHEMA
from sqlalchemy.sql import text

def seed_spells():
    fireball = Spell(
        name = "Fireball",
        spell_level = 1,
        range = "120 ft",
        duration = "Instantaneous",
        effect = "fire",
        hit_dice = "1d20",
        description = "You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage. A flammable object hit by this spell ignites if it isn't being worn or carried.",
        modifier = "gfgd",
        damage_dice = 4,
        saves = "Dexterity"
    )

    acid_splash = Spell(
        name = "Acid Splash",
        spell_level = 0,
        range = "60 ft",
        duration = "Instantaneous",
        effect = "acid",
        hit_dice = "1d20",
        description = "You hurl a bubble of acid. Choose one creature within range, or choose two creatures within range that are within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage.",
        modifier = "gfgd",
        damage_dice = 4,
        saves = "Dexterity",
    )

    db.session.add(fireball)
    db.session.add(acid_splash)
    db.session.commit()

def undo_spells():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.spells RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM spells"))

    db.session.commit()