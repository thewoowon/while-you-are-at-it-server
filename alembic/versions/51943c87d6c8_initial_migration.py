"""Initial migration

Revision ID: 51943c87d6c8
Revises: 
Create Date: 2024-12-13 22:18:26.673042

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51943c87d6c8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notification',
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('contents', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notification_id'), 'notification', ['id'], unique=False)
    op.create_table('service_category',
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_service_category_code'), 'service_category', ['code'], unique=False)
    op.create_index(op.f('ix_service_category_id'), 'service_category', ['id'], unique=False)
    op.create_table('store',
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('business_hours', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_store_id'), 'store', ['id'], unique=False)
    op.create_index(op.f('ix_store_name'), 'store', ['name'], unique=False)
    op.create_table('user',
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('nickname', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('src', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('article',
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('pick_up_location', sa.String(), nullable=True),
    sa.Column('pick_up_time', sa.String(), nullable=True),
    sa.Column('destination', sa.String(), nullable=True),
    sa.Column('departure_date_and_time', sa.String(), nullable=True),
    sa.Column('contents', sa.String(), nullable=True),
    sa.Column('number_of_recruits', sa.Integer(), nullable=True),
    sa.Column('process_status', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_article_id'), 'article', ['id'], unique=False)
    op.create_table('chat',
    sa.Column('founder_id', sa.Integer(), nullable=True),
    sa.Column('attendant_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['attendant_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['founder_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_chat_id'), 'chat', ['id'], unique=False)
    op.create_table('review',
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('contents', sa.String(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_review_id'), 'review', ['id'], unique=False)
    op.create_table('service',
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('unit', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('discount_rate', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_service_id'), 'service', ['id'], unique=False)
    op.create_table('delivery',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.Column('request_date', sa.String(), nullable=True),
    sa.Column('request_time', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_delivery_id'), 'delivery', ['id'], unique=False)
    op.create_table('message',
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('chat_id', sa.Integer(), nullable=True),
    sa.Column('sequence', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_id'), 'message', ['id'], unique=False)
    op.create_table('order',
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_id'), 'order', ['id'], unique=False)
    op.create_table('image',
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_image_id'), 'image', ['id'], unique=False)
    op.drop_table('Store')
    op.drop_table('Chat')
    op.drop_table('Order')
    op.drop_table('Notification')
    op.drop_table('Image')
    op.drop_table('Delivery')
    op.drop_table('User')
    op.drop_table('Message')
    op.drop_table('Review')
    op.drop_table('Service_Category')
    op.drop_table('Article')
    op.drop_table('Service')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Service',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('store_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.Column('unit', sa.TEXT(), nullable=False),
    sa.Column('price', sa.NUMERIC(), nullable=False),
    sa.Column('discount_rate', sa.NUMERIC(), nullable=False),
    sa.Column('type', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.NUMERIC(), nullable=False),
    sa.Column('updated_at', sa.NUMERIC(), nullable=False),
    sa.ForeignKeyConstraint(['store_id'], ['Store.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Article',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('type', sa.INTEGER(), nullable=False),
    sa.Column('pick_up_location', sa.TEXT(), nullable=False),
    sa.Column('pick_up_time', sa.TEXT(), nullable=False),
    sa.Column('destination', sa.TEXT(), nullable=False),
    sa.Column('departure_date_and_time', sa.TEXT(), nullable=False),
    sa.Column('title', sa.TEXT(), nullable=False),
    sa.Column('contents', sa.TEXT(), nullable=False),
    sa.Column('number_of_recruits', sa.INTEGER(), nullable=False),
    sa.Column('process_status', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.NUMERIC(), nullable=False),
    sa.Column('updated_at', sa.NUMERIC(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Service_Category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('code', sa.TEXT(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('created_at', sa.NUMERIC(), nullable=False),
    sa.Column('updated_at', sa.NUMERIC(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Review',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('store_id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.TEXT(), nullable=False),
    sa.Column('score', sa.INTEGER(), nullable=False),
    sa.Column('contents', sa.TEXT(), nullable=False),
    sa.Column('created_at', sa.NUMERIC(), nullable=False),
    sa.Column('updated_at', sa.NUMERIC(), nullable=False),
    sa.ForeignKeyConstraint(['store_id'], ['Store.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Message',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sender_id', sa.INTEGER(), nullable=False),
    sa.Column('chat_id', sa.INTEGER(), nullable=False),
    sa.Column('sequence', sa.INTEGER(), nullable=False),
    sa.Column('message', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.NUMERIC(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['Chat.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sender_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('nickname', sa.TEXT(), nullable=True),
    sa.Column('email', sa.TEXT(), nullable=False),
    sa.Column('phone_number', sa.TEXT(), nullable=True),
    sa.Column('address', sa.TEXT(), nullable=True),
    sa.Column('src', sa.TEXT(), nullable=True),
    sa.Column('create_at', sa.NUMERIC(), nullable=False),
    sa.Column('updated_at', sa.NUMERIC(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Delivery',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('article_id', sa.INTEGER(), nullable=False),
    sa.Column('request_date', sa.TEXT(), nullable=False),
    sa.Column('request_time', sa.TEXT(), nullable=False),
    sa.Column('created_at', sa.NUMERIC(), nullable=False),
    sa.Column('updated_at', sa.NUMERIC(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['Article.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Image',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('url', sa.TEXT(), nullable=False),
    sa.Column('type', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.NUMERIC(), nullable=False),
    sa.Column('updated_at', sa.NUMERIC(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Notification',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.TEXT(), nullable=False),
    sa.Column('contents', sa.TEXT(), nullable=False),
    sa.Column('created_at', sa.NUMERIC(), nullable=False),
    sa.Column('updated_at', sa.NUMERIC(), nullable=False),
    sa.Column('type', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Order',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('store_id', sa.INTEGER(), nullable=False),
    sa.Column('service_id', sa.INTEGER(), nullable=False),
    sa.Column('type', sa.INTEGER(), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.Column('created_at', sa.NUMERIC(), nullable=False),
    sa.Column('updated_at', sa.NUMERIC(), nullable=False),
    sa.ForeignKeyConstraint(['service_id'], ['Service.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['store_id'], ['Store.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Chat',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('founder_id', sa.INTEGER(), nullable=False),
    sa.Column('attendant_id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.NUMERIC(), nullable=False),
    sa.Column('updated_at', sa.NUMERIC(), nullable=False),
    sa.ForeignKeyConstraint(['attendant_id'], ['User.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['founder_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Store',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('address', sa.TEXT(), nullable=False),
    sa.Column('type', sa.INTEGER(), nullable=False),
    sa.Column('business_hours', sa.TEXT(), nullable=False),
    sa.Column('phone_number', sa.TEXT(), nullable=False),
    sa.Column('created_at', sa.NUMERIC(), nullable=False),
    sa.Column('updated_at', sa.NUMERIC(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index(op.f('ix_image_id'), table_name='image')
    op.drop_table('image')
    op.drop_index(op.f('ix_order_id'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_message_id'), table_name='message')
    op.drop_table('message')
    op.drop_index(op.f('ix_delivery_id'), table_name='delivery')
    op.drop_table('delivery')
    op.drop_index(op.f('ix_service_id'), table_name='service')
    op.drop_table('service')
    op.drop_index(op.f('ix_review_id'), table_name='review')
    op.drop_table('review')
    op.drop_index(op.f('ix_chat_id'), table_name='chat')
    op.drop_table('chat')
    op.drop_index(op.f('ix_article_id'), table_name='article')
    op.drop_table('article')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_store_name'), table_name='store')
    op.drop_index(op.f('ix_store_id'), table_name='store')
    op.drop_table('store')
    op.drop_index(op.f('ix_service_category_id'), table_name='service_category')
    op.drop_index(op.f('ix_service_category_code'), table_name='service_category')
    op.drop_table('service_category')
    op.drop_index(op.f('ix_notification_id'), table_name='notification')
    op.drop_table('notification')
    # ### end Alembic commands ###
