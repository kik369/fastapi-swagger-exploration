"""Added is_staff to User

Revision ID: 1d78fcf5e56e
Revises: 6fb89d18e77e
Create Date: 2024-02-18 16:02:35.933165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d78fcf5e56e'
down_revision: Union[str, None] = '6fb89d18e77e'
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