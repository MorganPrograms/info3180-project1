"""empty message

Revision ID: 2c5acc2f1f54
Revises: 
Create Date: 2020-03-11 11:43:13.849172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c5acc2f1f54'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('First_name', sa.String(length=80), nullable=True),
    sa.Column('Last_name', sa.String(length=80), nullable=True),
    sa.Column('Gender', sa.String(length=6), nullable=True),
    sa.Column('Email', sa.String(length=80), nullable=True),
    sa.Column('Location', sa.String(length=80), nullable=True),
    sa.Column('Biography', sa.String(length=255), nullable=True),
    sa.Column('File', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Profiles')
    # ### end Alembic commands ###
