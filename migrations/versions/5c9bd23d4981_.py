"""empty message

Revision ID: 5c9bd23d4981
Revises: df4cc22bb535
Create Date: 2020-12-23 12:29:46.834359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c9bd23d4981'
down_revision = 'df4cc22bb535'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.drop_column('Artist', 'seeking_talent')
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.add_column('Artist', sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###
