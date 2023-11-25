from app.models import db, Skill, environment, SCHEMA
from sqlalchemy.sql import text

def seed_skills():
    skill1 = Skill(
        name = 'Sleight of Hand',
        description = "Whenever you attempt an act of legerdemain or manual trickery, such as planting something on someone else or concealing an object on your person, make a Dexterity (Sleight of Hand) check. The GM might also call for a Dexterity (Sleight of Hand) check to determine whether you can lift a coin purse off another person or slip something out of another person's pocket."
    )

    skill2 = Skill(
        name = 'Stealth',
        description = "Make a Dexterity (Stealth) check when you attempt to conceal yourself from enemies, slink past guards, slip away without being noticed, or sneak up on someone without being seen or heard."
    )

    db.session.add(skill1)
    db.session.add(skill2)
    db.session.commit()

def undo_skills():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.skills RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM skills"))

    db.session.commit()