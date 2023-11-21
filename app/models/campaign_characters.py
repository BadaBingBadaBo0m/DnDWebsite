from .db import db, environment, SCHEMA, add_prefix_for_prod

campaign_characters = db.Table(
    'campaign_characters',
    db.Model.metadata,
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('campaign_id', db.Integer, db.ForeignKey(add_prefix_for_prod('campaigns.id'))),
    db.Column('character_id', db.Integer, db.ForeignKey(add_prefix_for_prod('characters.id')))
)