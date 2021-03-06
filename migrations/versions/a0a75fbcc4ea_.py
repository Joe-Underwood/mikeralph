"""empty message

Revision ID: a0a75fbcc4ea
Revises: ddb6424f20f9
Create Date: 2021-08-30 13:11:07.076833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0a75fbcc4ea'
down_revision = 'ddb6424f20f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product__image', sa.Column('priority', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product__image', 'priority')
    # ### end Alembic commands ###
