"""remove category_id and supplier_id columns

Revision ID: fix_remove_columns_20260218
Revises: b93634803bde
Create Date: 2026-02-17 21:38:30.026589

"""

from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = "fix_remove_columns_20260218"
down_revision: Union[str, Sequence[str], None] = "b93634803bde"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
