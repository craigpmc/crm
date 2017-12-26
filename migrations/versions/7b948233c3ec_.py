"""empty message

Revision ID: 7b948233c3ec
Revises: 2aea228edd39
Create Date: 2017-12-26 18:50:46.370204

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7b948233c3ec'
down_revision = '2aea228edd39'
branch_labels = None
depends_on = None

old_dealtype = postgresql.ENUM('HOSTER', 'ITO', 'PTO', 'AMBASSADOR', 'ITFT', name='dealtype')
new_dealtype = postgresql.ENUM('HOSTER', 'ITO', 'PTO', 'AMBASSADOR', 'ITFT', 'PREPTO', name='dealtype')
temp_new_dealtype = postgresql.ENUM('HOSTER', 'ITO', 'PTO', 'AMBASSADOR', 'ITFT' , 'PREPTO', name='_dealtype')

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activities',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.String(length=5), nullable=False),
    sa.Column('type', sa.Enum('ISSUE_TF_APP', 'ISSUE_IYO', 'ISSUE_EXTRANET', 'INFO_WAITING', 'KYC', 'QUESTION_LEGAL', 'QUESTION_PROCESS', 'QUESTION_FINANCE', 'QUESTION', 'MEETING_WAITING', 'ZOOM_WAITING', name='activitytype'), nullable=True),
    sa.Column('author_last_id', sa.String(length=5), nullable=True),
    sa.Column('author_original_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['author_last_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['author_original_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_activities_type'), 'activities', ['type'], unique=True)
    op.create_table('contacts_activities',
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('activity_id', sa.String(length=5), nullable=True),
    sa.Column('contact_id', sa.String(length=5), nullable=True),
    sa.Column('author_last_id', sa.String(length=5), nullable=True),
    sa.Column('author_original_id', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['activities.id'], ),
    sa.ForeignKeyConstraint(['author_last_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['author_original_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    temp_new_dealtype.create(op.get_bind(), checkfirst=False)
    op.execute('ALTER TABLE deals ALTER COLUMN deal_type TYPE _dealtype'
               ' USING deal_type::text::_dealtype')

    old_dealtype.drop(op.get_bind(), checkfirst=False)
    # Create and convert to the "new" status type
    new_dealtype.create(op.get_bind(), checkfirst=False)

    op.execute('ALTER TABLE deals ALTER COLUMN deal_type TYPE dealtype'
               ' USING deal_type::text::dealtype')

    temp_new_dealtype.drop(op.get_bind(), checkfirst=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts_activities')
    op.drop_index(op.f('ix_activities_type'), table_name='activities')
    op.drop_table('activities')
    # ### end Alembic commands ###
