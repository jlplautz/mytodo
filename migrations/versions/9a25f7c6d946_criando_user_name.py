"""Criando user_name
Revision ID: 9a25f7c6d946
Revises: 67faedd1a399
Create Date: 2023-08-03 19:18:25.488718
"""
import sqlalchemy as sa
import sqlmodel
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9a25f7c6d946'
down_revision = '67faedd1a399'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'user',
        sa.Column(
            'user_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
    )
    op.alter_column(
        'user',
        'updated_at',
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
    )
    op.create_unique_constraint(None, 'user', ['user_name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column(
        'user',
        'updated_at',
        existing_type=postgresql.TIMESTAMP(),
        nullable=True,
    )
    op.drop_column('user', 'user_name')
    # ### end Alembic commands ###
