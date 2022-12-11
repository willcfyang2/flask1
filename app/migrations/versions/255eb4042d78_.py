"""empty message

Revision ID: 255eb4042d78
Revises: 3978b9975f8c
Create Date: 2022-12-03 15:24:47.698482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '255eb4042d78'
down_revision = '3978b9975f8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('images', sa.Column('comment', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('images', 'comment')
    # ### end Alembic commands ###