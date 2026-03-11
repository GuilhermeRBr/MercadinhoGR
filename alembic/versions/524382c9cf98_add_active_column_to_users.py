"""add active column to users

Revision ID: 524382c9cf98
Revises: 6f11c99b7f14
Create Date: 2026-03-11 16:38:18.466167

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "524382c9cf98"
down_revision: Union[str, Sequence[str], None] = "6f11c99b7f14"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("active", sa.Boolean(), nullable=False, server_default=sa.true()),
    )


def downgrade() -> None:
    op.drop_column("users", "active")
