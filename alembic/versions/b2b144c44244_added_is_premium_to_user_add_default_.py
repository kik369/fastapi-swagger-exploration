"""Added is_premium to User. Add default False value.

Revision ID: b2b144c44244
Revises: e42fc8e763f0
Create Date: 2024-02-18 16:11:50.268613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2b144c44244'
down_revision: Union[str, None] = 'e42fc8e763f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
