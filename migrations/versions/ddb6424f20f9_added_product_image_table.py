"""added product_image table

Revision ID: ddb6424f20f9
Revises: b80f972c5722
Create Date: 2021-08-30 13:10:37.729192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddb6424f20f9'
down_revision = 'b80f972c5722'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=64), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('img_filename', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('priority'),
    sa.UniqueConstraint('product_name')
    )
    op.create_table('product__image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img_filename', sa.String(length=64), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product__subtype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('width', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('length', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('height', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product__subtype')
    op.drop_table('product__image')
    op.drop_table('product')
    # ### end Alembic commands ###
