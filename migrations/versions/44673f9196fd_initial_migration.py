"""initial migration

Revision ID: 44673f9196fd
Revises: 99eacccaab18
Create Date: 2022-07-12 14:10:49.672587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44673f9196fd'
down_revision = '99eacccaab18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###