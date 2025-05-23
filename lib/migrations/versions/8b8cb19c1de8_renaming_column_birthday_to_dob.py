"""Renaming column birthday to dob

Revision ID: 8b8cb19c1de8
Revises: 791279dd0760
Create Date: 2025-05-23 17:09:40.198347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b8cb19c1de8'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students','birthday',new_column_name='dob')


def downgrade() -> None:
    op.alter_column('students','dob',new_column_name='birthday')
