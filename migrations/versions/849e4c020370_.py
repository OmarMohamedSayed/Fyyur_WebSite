"""empty message

Revision ID: 849e4c020370
Revises: 8865c8420159
Create Date: 2020-12-21 15:13:21.356015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '849e4c020370'
down_revision = '8865c8420159'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('website', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'website')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    # ### end Alembic commands ###
