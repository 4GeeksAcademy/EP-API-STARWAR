"""empty message

Revision ID: 030e1e6407e8
Revises: a5cffa318ac2
Create Date: 2024-11-11 23:50:25.671572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '030e1e6407e8'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('eye_color', sa.String(length=250), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('gravity', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(length=250), nullable=False),
    sa.Column('climate', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_planet', sa.Integer(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_people', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_people'], ['people.id'], ),
    sa.ForeignKeyConstraint(['id_planet'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=250), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=250), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=250),
               existing_nullable=False)
        batch_op.drop_constraint('user_email_key', type_='unique')
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.create_unique_constraint('user_email_key', ['email'])
        batch_op.alter_column('password',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('last_name')
        batch_op.drop_column('name')

    op.drop_table('favorites')
    op.drop_table('planet')
    op.drop_table('people')
    # ### end Alembic commands ###
