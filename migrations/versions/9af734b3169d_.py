"""empty message

Revision ID: 9af734b3169d
Revises: 9a25f7c6d946
Create Date: 2023-10-26 13:32:09.954892
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '9af734b3169d'
down_revision = '9a25f7c6d946'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('super_user', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'super_user')
    # ### end Alembic commands ###