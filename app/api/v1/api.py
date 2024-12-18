from fastapi import APIRouter
from app.api.v1.endpoints import user, article, chat, delivery, image, message, notification, order, review, service_category, service, store

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(
    article.router, prefix="/articles", tags=["articles"])
api_router.include_router(chat.router, prefix="/chats", tags=["chats"])
api_router.include_router(
    delivery.router, prefix="/deliveries", tags=["deliveries"])
api_router.include_router(image.router, prefix="/images", tags=["images"])
api_router.include_router(
    message.router, prefix="/messages", tags=["messages"])
api_router.include_router(
    notification.router, prefix="/notifications", tags=["notifications"])
api_router.include_router(order.router, prefix="/orders", tags=["orders"])
api_router.include_router(review.router, prefix="/reviews", tags=["reviews"])
# api_router.include_router(service_category.router,
#                           prefix="/service_categories", tags=["service_categories"])
api_router.include_router(
    service.router, prefix="/services", tags=["services"])
api_router.include_router(store.router, prefix="/stores", tags=["stores"])
