"""empty message

Revision ID: 3befacdb3d24
Revises: 030e1e6407e8
Create Date: 2024-11-12 01:53:27.007621

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3befacdb3d24'
down_revision = '030e1e6407e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('gravity', sa.String(length=50), nullable=True),
    sa.Column('terrain', sa.String(length=100), nullable=True),
    sa.Column('climate', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('user')
    op.drop_table('planet')
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint('favorites_id_planet_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorites_id_user_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'planets', ['id_planet'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['id_user'], ['id'])

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=250),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('height',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.String(length=50),
               nullable=True)
        batch_op.alter_column('eye_color',
               existing_type=sa.VARCHAR(length=250),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('mass',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=50),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.alter_column('mass',
               existing_type=sa.String(length=50),
               type_=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('eye_color',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=250),
               existing_nullable=True)
        batch_op.alter_column('height',
               existing_type=sa.String(length=50),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=250),
               existing_nullable=False)

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favorites_id_user_fkey', 'user', ['id_user'], ['id'])
        batch_op.create_foreign_key('favorites_id_planet_fkey', 'planet', ['id_planet'], ['id'])

    op.create_table('planet',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('gravity', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('terrain', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('climate', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='planet_pkey')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.drop_table('users')
    op.drop_table('planets')
    # ### end Alembic commands ###
