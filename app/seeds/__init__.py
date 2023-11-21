from flask.cli import AppGroup
from .users import seed_users, undo_users
from .characters import seed_characters, undo_characters
from .spells import seed_spells, undo_spells
from .character_spells import seed_character_spells, undo_character_spells
from .skills import seed_skills, undo_skills
from .character_skills import seed_character_skills, undo_character_skills
from .races import seed_races, undo_races
from .items import seed_items, undo_items
from .character_inventories import seed_character_inventories, undo_character_inventories
from .character_feats import seed_character_feats, undo_character_feats
from .campaigns import seed_campaigns, undo_campaigns
from .campaign_characters import seed_campaign_characters, undo_campaign_characters

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo 
        # command, which will  truncate all tables prefixed with 
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_character_inventories()
        undo_campaign_characters()
        undo_character_feats()
        undo_character_skills()
        undo_character_spells()
        undo_items()
        undo_skills()
        undo_spells()
        undo_characters()
        undo_races()
        undo_campaigns()
        undo_users()
    seed_users()
    seed_campaigns()
    seed_races()
    seed_items()
    seed_spells()
    seed_skills()
    seed_characters()
    seed_character_spells()
    seed_character_skills()
    seed_character_feats()
    seed_campaign_characters()
    seed_character_inventories()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_character_inventories()
    undo_campaign_characters()
    undo_character_feats()
    undo_character_skills()
    undo_character_spells()
    undo_races()
    undo_skills()
    undo_items()
    undo_spells()
    undo_characters()
    undo_campaigns()
    undo_users()
    # Add other undo functions here