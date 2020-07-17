"""Pitches table

Revision ID: 882158a44918
Revises: 30e4a0416dd5
Create Date: 2020-07-17 19:09:23.393647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '882158a44918'
down_revision = '30e4a0416dd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    # ### end Alembic commands ###