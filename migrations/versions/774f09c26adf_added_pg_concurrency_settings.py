"""Added PG CONCURRENCY SETTINGS

Revision ID: 774f09c26adf
Revises:
Create Date: 2024-06-26 18:53:44.433410

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "774f09c26adf"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "concurrency",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("Создана ли схема таблиц в БД.", sa.Boolean(), nullable=False),
        sa.Column("Текущий уровень изоляции", sa.SmallInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_concurrency_id"), "concurrency", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_concurrency_id"), table_name="concurrency")
    op.drop_table("concurrency")
    # ### end Alembic commands ###