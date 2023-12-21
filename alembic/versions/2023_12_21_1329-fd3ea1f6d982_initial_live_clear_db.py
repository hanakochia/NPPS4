"""Initial live clear DB

Revision ID: fd3ea1f6d982
Revises: 7d1d47012d0c
Create Date: 2023-12-21 13:29:45.799865

"""
import itertools
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm.session import Session

import npps4.db.main


# revision identifiers, used by Alembic.
revision: str = "fd3ea1f6d982"
down_revision: Union[str, None] = "7d1d47012d0c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "live_clear",
        sa.Column("id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("user_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("live_difficulty_id", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("hi_score", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("hi_combo_cnt", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.Column("clear_cnt", sa.BigInteger().with_variant(sa.INTEGER(), "sqlite"), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "live_difficulty_id"),
    )
    with op.batch_alter_table("live_clear", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_live_clear_live_difficulty_id"), ["live_difficulty_id"], unique=False)
        batch_op.create_index(batch_op.f("ix_live_clear_user_id"), ["user_id"], unique=False)

    with Session(bind=op.get_bind()) as session:
        users = list(session.execute(sa.select(npps4.db.main.User)).scalars())

        for user in users:
            for live_difficulty_id in itertools.chain(range(1, 4), (350,), range(1190, 1226)):
                live = npps4.db.main.LiveClear(user_id=user.id, live_difficulty_id=live_difficulty_id)
                session.add(live)

        session.commit()

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("live_clear", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_live_clear_user_id"))
        batch_op.drop_index(batch_op.f("ix_live_clear_live_difficulty_id"))

    op.drop_table("live_clear")
    # ### end Alembic commands ###
