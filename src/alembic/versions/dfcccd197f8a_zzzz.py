"""zzzz

Revision ID: dfcccd197f8a
Revises: 48336e91271d
Create Date: 2023-02-24 23:00:44.496517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfcccd197f8a'
down_revision = '48336e91271d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_Operations_created_by'), 'Operations', ['created_by'], unique=False)
    op.create_index(op.f('ix_Operations_modified_by'), 'Operations', ['modified_by'], unique=False)
    op.create_foreign_key(None, 'Operations', 'Users', ['modified_by'], ['id'])
    op.create_foreign_key(None, 'Operations', 'Users', ['created_by'], ['id'])
    op.create_index(op.f('ix_Products_created_by'), 'Products', ['created_by'], unique=False)
    op.create_index(op.f('ix_Products_modified_by'), 'Products', ['modified_by'], unique=False)
    op.create_foreign_key(None, 'Products', 'Users', ['modified_by'], ['id'])
    op.create_foreign_key(None, 'Products', 'Users', ['created_by'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Products', type_='foreignkey')
    op.drop_constraint(None, 'Products', type_='foreignkey')
    op.drop_index(op.f('ix_Products_modified_by'), table_name='Products')
    op.drop_index(op.f('ix_Products_created_by'), table_name='Products')
    op.drop_constraint(None, 'Operations', type_='foreignkey')
    op.drop_constraint(None, 'Operations', type_='foreignkey')
    op.drop_index(op.f('ix_Operations_modified_by'), table_name='Operations')
    op.drop_index(op.f('ix_Operations_created_by'), table_name='Operations')
    # ### end Alembic commands ###