from app.models import db, Character_Class, environment, SCHEMA
from sqlalchemy.sql import text

def seed_classes():
    fighter = Character_Class(
        name = 'Fighter',
        description = "Fighters learn the basics of all combat styles. Every fighter can swing an axe, fence with a rapier, wield a longsword or a greatsword, use a bow, and even trap foes in a net with some degree of skill.",
        hit_points = 10,
        hit_dice = "1d10",
        hit_point_modifier = "1d10 or 6"
    )
    wizard = Character_Class(
        name = 'Wizard',
        description = "Wild and enigmatic, varied in form and function, the power of magic draws students who seek to master its mysteries. Some aspire to become like the gods, shaping reality itself.",
        hit_points = 6,
        hit_dice = "1d6",
        hit_point_modifier = "1d6 or 4"
    )

    db.session.add(fighter)
    db.session.add(wizard)
    db.session.commit()

def undo_classes():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.classes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM classes"))

    db.session.commit()