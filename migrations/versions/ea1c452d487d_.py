"""empty message

Revision ID: ea1c452d487d
Revises: 00d85ae0cfdb
Create Date: 2023-11-20 20:22:48.103230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea1c452d487d'
down_revision = '00d85ae0cfdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('damage', sa.String(length=100), nullable=True),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    # ### end Alembic commands ###
