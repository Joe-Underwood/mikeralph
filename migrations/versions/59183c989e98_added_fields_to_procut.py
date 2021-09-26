"""added fields to Procut

Revision ID: 59183c989e98
Revises: 4e5c52775944
Create Date: 2021-08-29 12:15:06.264969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59183c989e98'
down_revision = '4e5c52775944'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('leg_height', sa.Numeric(precision=10, scale=2), nullable=True))
    op.add_column('product', sa.Column('with_legs', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'with_legs')
    op.drop_column('product', 'leg_height')
    # ### end Alembic commands ###
