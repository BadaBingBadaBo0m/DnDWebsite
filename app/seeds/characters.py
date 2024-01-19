from app.models import db, Character, environment, SCHEMA
from sqlalchemy.sql import text


def seed_characters():
    character1 = Character(
        name='Bruh', gender='Male', description='I am a bruh')
    character2 = Character(
        name='Whatchu Mean', gender='Female', description='I am a whatchu mean')

    db.session.add(character1)
    db.session.add(character2)
    db.session.commit()

def undo_characters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.characters RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM characters"))
        
    db.session.commit()