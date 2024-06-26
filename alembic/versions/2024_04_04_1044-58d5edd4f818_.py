"""empty message

Revision ID: 58d5edd4f818
Revises: 5039725fabc6
Create Date: 2024-04-04 10:44:23.813581

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "58d5edd4f818"
down_revision: Union[str, None] = "5039725fabc6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "item",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("item_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("item", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_item_item_id"), ["item_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_item_user_id"), ["user_id"], unique=True)

    op.create_table(
        "recovery_item",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("item_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("recovery_item", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_recovery_item_item_id"), ["item_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_recovery_item_user_id"), ["user_id"], unique=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("recovery_item", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_recovery_item_user_id"))
        batch_op.drop_index(batch_op.f("ix_recovery_item_item_id"))

    op.drop_table("recovery_item")
    with op.batch_alter_table("item", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_item_user_id"))
        batch_op.drop_index(batch_op.f("ix_item_item_id"))

    op.drop_table("item")
    # ### end Alembic commands ###
