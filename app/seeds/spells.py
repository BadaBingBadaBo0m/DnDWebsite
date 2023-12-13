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
        damage_at_slot_level = "3:8d6, 4:9d6, 5:10d6, 6:11d6, 7:12d6, 8:13d6, 9:14d6"
    )
    acid_arrow = Spell(
        name = "Acid-Arrow",
        description = "A shimmering green arrow streaks toward a target within range and bursts in a spray of acid. Make a ranged spell attack against the target. On a hit, the target takes 4d4 acid damage immediately and 2d4 acid damage at the end of its next turn. On a miss, the arrow splashes the target with acid for half as much of the initial damage and no damage at the end of its next turn.",
        range = "90 feet",
        duration = "Instantaneous",
        components = "V, S, M",
        ritual = False,
        concentration = False,
        casting_time = "1 action",
        damage_at_slot_level = "2:4d4, 3:5d4, 4:6d4, 5:7d4, 6:8d4, 7:9d4, 8:10d4, 9:11d4"
    )

    db.session.add(fireball)
    db.session.add(acid_arrow)
    
    db.session.commit()

def undo_spells():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.spells RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM spells"))

    db.session.commit()