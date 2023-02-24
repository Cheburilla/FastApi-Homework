"""z

Revision ID: 9462d2eb5c03
Revises: 
Create Date: 2023-02-24 21:42:18.875561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9462d2eb5c03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_Tanks_created_by'), 'Tanks', ['created_by'], unique=False)
    op.create_index(op.f('ix_Tanks_modified_by'), 'Tanks', ['modified_by'], unique=False)
    op.create_foreign_key(None, 'Tanks', 'Users', ['created_by'], ['id'])
    op.create_foreign_key(None, 'Tanks', 'Users', ['modified_by'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Tanks', type_='foreignkey')
    op.drop_constraint(None, 'Tanks', type_='foreignkey')
    op.drop_index(op.f('ix_Tanks_modified_by'), table_name='Tanks')
    op.drop_index(op.f('ix_Tanks_created_by'), table_name='Tanks')
    # ### end Alembic commands ###