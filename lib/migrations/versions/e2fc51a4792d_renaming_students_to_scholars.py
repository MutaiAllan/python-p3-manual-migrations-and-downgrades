"""Renaming students to scholars

Revision ID: e2fc51a4792d
Revises: 791279dd0760
Create Date: 2023-09-14 13:43:18.721659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2fc51a4792d'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
