"""empty message

Revision ID: 1cdd62d14df4
Revises: 
Create Date: 2020-06-04 20:57:25.181834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cdd62d14df4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('journal_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('entry_type', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_journal_entry_timestamp'), 'journal_entry', ['timestamp'], unique=False)
    op.create_table('station',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ref_id', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('owner', sa.String(length=64), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=6, scale=4), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=7, scale=4), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('air_quality_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('PM10', sa.Numeric(precision=4, scale=1), nullable=True),
    sa.Column('PM2_5', sa.Numeric(precision=4, scale=1), nullable=True),
    sa.Column('O3', sa.Numeric(precision=4, scale=1), nullable=True),
    sa.Column('NO_', sa.Numeric(precision=4, scale=1), nullable=True),
    sa.Column('NO2', sa.Numeric(precision=4, scale=1), nullable=True),
    sa.Column('NOx', sa.Numeric(precision=4, scale=1), nullable=True),
    sa.Column('AQI', sa.Numeric(precision=3, scale=0), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['journal_entry.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hydrologic_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('water_level', sa.Numeric(precision=3, scale=1), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['journal_entry.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('indoor_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('temperature', sa.Numeric(precision=3, scale=1), nullable=True),
    sa.Column('humidity', sa.Numeric(precision=4, scale=1), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['journal_entry.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('synoptic_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('temperature', sa.Numeric(precision=3, scale=1), nullable=True),
    sa.Column('pressure', sa.Numeric(precision=5, scale=1), nullable=True),
    sa.Column('humidity', sa.Numeric(precision=4, scale=1), nullable=True),
    sa.Column('precipitation', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('wind_speed', sa.Numeric(precision=3, scale=0), nullable=True),
    sa.Column('wind_azimuth', sa.Numeric(precision=3, scale=0), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['journal_entry.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('synoptic_entry')
    op.drop_table('indoor_entry')
    op.drop_table('hydrologic_entry')
    op.drop_table('air_quality_entry')
    op.drop_table('station')
    op.drop_index(op.f('ix_journal_entry_timestamp'), table_name='journal_entry')
    op.drop_table('journal_entry')
    # ### end Alembic commands ###
