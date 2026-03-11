"""add active column to products

Revision ID: 6f11c99b7f14
Revises: f557e239f6b0
Create Date: 2026-03-11 14:48:52.897884

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "6f11c99b7f14"
down_revision: Union[str, Sequence[str], None] = "f557e239f6b0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "products",
        sa.Column("active", sa.Boolean(), nullable=False, server_default=sa.true()),
    )


def downgrade() -> None:
    op.drop_column("products", "active")
