"""add content column to posts table

Revision ID: c442c86ef6e7
Revises: 8ac18a25a9d4
Create Date: 2026-07-24 16:16:18.329891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c442c86ef6e7'
down_revision: Union[str, Sequence[str], None] = '8ac18a25a9d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
