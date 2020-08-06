"""Initial migration

Revision ID: 93a5ab3e4b4f
Create Date: 2020-08-02 12:15:22.759416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93a5ab3e4b4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('messages',
        sa.Column('message_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('value', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('message_id')
    )
    op.create_table('user',
        sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('username', sa.Integer(), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('user_id')
    )


def downgrade():
    op.drop_table('user')
    op.drop_table('messages')
