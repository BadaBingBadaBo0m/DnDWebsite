from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Campaign(db.Model):
    __tablename__ = 'campaigns'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    # Owner id foreign key
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
