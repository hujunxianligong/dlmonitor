"""empty message

Revision ID: 220426586e09
Revises: f021f3df44c3
Create Date: 2017-06-12 23:11:24.491957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '220426586e09'
down_revision = 'f021f3df44c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('arxiv', sa.Column('analyzed', sa.Boolean(), server_default='false', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('arxiv', 'analyzed')
    # ### end Alembic commands ###
