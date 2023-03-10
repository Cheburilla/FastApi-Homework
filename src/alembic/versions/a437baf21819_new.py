"""new

Revision ID: a437baf21819
Revises: 
Create Date: 2023-02-26 17:12:13.852775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a437baf21819'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('modified_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['Users.id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Users_created_by'), 'Users', ['created_by'], unique=False)
    op.create_index(op.f('ix_Users_modified_by'), 'Users', ['modified_by'], unique=False)
    op.create_table('Products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('modified_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['Users.id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Products_created_by'), 'Products', ['created_by'], unique=False)
    op.create_index(op.f('ix_Products_modified_by'), 'Products', ['modified_by'], unique=False)
    op.create_table('Tanks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('max_capacity', sa.Float(), nullable=True),
    sa.Column('current_capacity', sa.Float(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('modified_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['Users.id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['Users.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['Products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Tanks_created_by'), 'Tanks', ['created_by'], unique=False)
    op.create_index(op.f('ix_Tanks_modified_by'), 'Tanks', ['modified_by'], unique=False)
    op.create_index(op.f('ix_Tanks_product_id'), 'Tanks', ['product_id'], unique=False)
    op.create_table('Operations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mass', sa.Float(), nullable=True),
    sa.Column('date_start', sa.DateTime(), nullable=True),
    sa.Column('date_end', sa.DateTime(), nullable=True),
    sa.Column('tank_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('modified_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['Users.id'], ),
    sa.ForeignKeyConstraint(['modified_by'], ['Users.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['Products.id'], ),
    sa.ForeignKeyConstraint(['tank_id'], ['Tanks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Operations_created_by'), 'Operations', ['created_by'], unique=False)
    op.create_index(op.f('ix_Operations_modified_by'), 'Operations', ['modified_by'], unique=False)
    op.create_index(op.f('ix_Operations_product_id'), 'Operations', ['product_id'], unique=False)
    op.create_index(op.f('ix_Operations_tank_id'), 'Operations', ['tank_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Operations_tank_id'), table_name='Operations')
    op.drop_index(op.f('ix_Operations_product_id'), table_name='Operations')
    op.drop_index(op.f('ix_Operations_modified_by'), table_name='Operations')
    op.drop_index(op.f('ix_Operations_created_by'), table_name='Operations')
    op.drop_table('Operations')
    op.drop_index(op.f('ix_Tanks_product_id'), table_name='Tanks')
    op.drop_index(op.f('ix_Tanks_modified_by'), table_name='Tanks')
    op.drop_index(op.f('ix_Tanks_created_by'), table_name='Tanks')
    op.drop_table('Tanks')
    op.drop_index(op.f('ix_Products_modified_by'), table_name='Products')
    op.drop_index(op.f('ix_Products_created_by'), table_name='Products')
    op.drop_table('Products')
    op.drop_index(op.f('ix_Users_modified_by'), table_name='Users')
    op.drop_index(op.f('ix_Users_created_by'), table_name='Users')
    op.drop_table('Users')
    # ### end Alembic commands ###
