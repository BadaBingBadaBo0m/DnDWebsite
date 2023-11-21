"""empty message

Revision ID: 5bed1c506352
Revises: 1f67821e7f4a
Create Date: 2023-11-20 22:53:48.396467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bed1c506352'
down_revision = '1f67821e7f4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('campaigns',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('campaign_characters',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('campaign_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaigns.id'], ),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('campaign_characters')
    op.drop_table('campaigns')
    # ### end Alembic commands ###
