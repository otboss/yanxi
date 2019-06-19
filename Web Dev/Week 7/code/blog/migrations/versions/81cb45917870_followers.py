"""followers

Revision ID: 81cb45917870
Revises: a4729869c05d
Create Date: 2019-06-17 20:52:31.302477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81cb45917870'
down_revision = 'a4729869c05d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
