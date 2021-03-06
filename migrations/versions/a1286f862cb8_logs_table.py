"""logs table

Revision ID: a1286f862cb8
Revises: 
Create Date: 2020-06-19 11:24:36.032424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1286f862cb8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logger', sa.String(), nullable=True),
    sa.Column('level', sa.String(), nullable=True),
    sa.Column('message', sa.String(), nullable=True),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('method', sa.String(), nullable=True),
    sa.Column('ip', sa.String(), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sqlite_autoincrement=True
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log')
    # ### end Alembic commands ###
