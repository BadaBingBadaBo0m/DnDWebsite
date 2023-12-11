"""empty message

Revision ID: 042ec3690681
Revises: 312bc4c34e40
Create Date: 2023-12-10 18:06:16.330700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '042ec3690681'
down_revision = '312bc4c34e40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('descripton', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descripton'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('skills')
    # ### end Alembic commands ###