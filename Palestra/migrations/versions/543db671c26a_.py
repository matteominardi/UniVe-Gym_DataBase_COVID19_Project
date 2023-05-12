"""empty message

Revision ID: 543db671c26a
Revises: 7fef96fc51a7
Create Date: 2021-05-04 16:26:45.949057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '543db671c26a'
down_revision = '7fef96fc51a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('utenti',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('cognome', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('dataNascita', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('cars')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('model', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('doors', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='cars_pkey')
    )
    op.drop_table('utenti')
    # ### end Alembic commands ###