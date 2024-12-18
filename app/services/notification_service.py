from sqlalchemy.orm import Session
from app.schemas.notification import NotificationUpdate, NotificationResponse, NotificationCreate
from app.models.notification import Notification
from typing import List
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def create_notification(db: Session, user_id: int, notification: NotificationCreate):
    db_notification = Notification(
        title=notification.title,
        contents=notification.contents,
        notification_type=notification.notification_type,
        status=notification.status,
        user_id=user_id
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return NotificationResponse.model_validate(db_notification)


def update_notification(db: Session, notification_id: int, notification: NotificationUpdate):
    db_notification = db.query(Notification).filter(
        Notification.id == notification_id).first()
    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    db_notification.status = notification.status if notification.status else db_notification.status
    db.commit()
    db.refresh(db_notification)
    return NotificationResponse.model_validate(db_notification)


def delete_notification(db: Session, notification_id: int):
    db_notification = db.query(Notification).filter(
        Notification.id == notification_id).first()
    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    db.delete(db_notification)
    db.commit()
    return JSONResponse(content={"message": "Notification deleted successfully"}, status_code=200)


def get_notification_by_id(db: Session, notification_id: int):
    db_notification = db.query(Notification).filter(
        Notification.id == notification_id).first()
    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return NotificationResponse.model_validate(db_notification)


def get_notification_by_user_id(db: Session, user_id: int):
    db_notifications = db.query(Notification).filter(
        Notification.user_id == user_id).all()
    if not db_notifications:
        return []
    return [NotificationResponse.model_validate(notification) for notification in db_notifications]
