"""Renaming grade to points

Revision ID: b89fcfaf4596
Revises: e2fc51a4792d
Create Date: 2023-09-14 17:56:52.736140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b89fcfaf4596'
down_revision = 'e2fc51a4792d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'grade', points=sa.Column('points', sa.String(255)))


def downgrade() -> None:
    op.alter_column('scholars', 'points', points=sa.Column('points', sa.String(255)))
