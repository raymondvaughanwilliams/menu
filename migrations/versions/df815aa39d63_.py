"""empty message

Revision ID: df815aa39d63
Revises: 6eee0e4a14ab
Create Date: 2023-08-30 08:48:55.841895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df815aa39d63'
down_revision = '6eee0e4a14ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('phone_mobile', sa.String(length=20), nullable=True),
    sa.Column('phone_mobile2', sa.String(length=20), nullable=True),
    sa.Column('phone_home', sa.String(length=20), nullable=True),
    sa.Column('phone_home2', sa.String(length=20), nullable=True),
    sa.Column('phone_business', sa.String(length=20), nullable=True),
    sa.Column('phone_business2', sa.String(length=20), nullable=True),
    sa.Column('phone_other', sa.String(length=20), nullable=True),
    sa.Column('contact_url', sa.String(length=200), nullable=True),
    sa.Column('entity_id', sa.Integer(), nullable=True),
    sa.Column('entity_type', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_contacts'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts')
    # ### end Alembic commands ###
