"""Changed user_name from integer to string

Revision ID: 6cb2be06cf51
Revises: 93a5ab3e4b4f
Create Date: 2020-08-06 20:14:01.565260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cb2be06cf51'
down_revision = '93a5ab3e4b4f'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('user', 'username')
    op.add_column('user', sa.Column('username', sa.String(length=255), nullable=False))
    


def downgrade():
    op.drop_column('user', 'username')
    op.add_column('user', sa.Column('username', sa.String(length=255), nullable=False))
