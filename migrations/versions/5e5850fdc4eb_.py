"""empty message

Revision ID: 5e5850fdc4eb
Revises: 86a6b83b4f20
Create Date: 2023-10-11 10:03:13.343359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e5850fdc4eb'
down_revision = '86a6b83b4f20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('eggs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('weight', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('eggs', schema=None) as batch_op:
        batch_op.drop_column('weight')

    # ### end Alembic commands ###
