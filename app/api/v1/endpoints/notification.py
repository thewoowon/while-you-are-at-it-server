# 알림 생성
# 알림 조회
# 알림 삭제
# 알림 수정
# 알림 읽음 처리

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.notification import NotificationUpdate, NotificationResponse
from app.services.notification_service import get_notification_by_user_id, get_notification_by_id, update_notification, delete_notification
from app.dependencies import get_db

router = APIRouter()


@router.post("/", response_model=NotificationResponse)
def read_one(notification_id: int, db: Session = Depends(get_db)):
    return get_notification_by_id(db=db, notification_id=notification_id)


@router.post("/", response_model=NotificationResponse)
def read_all(user_id: int, db: Session = Depends(get_db)):
    return get_notification_by_user_id(db=db, user_id=user_id)


def update(notification_id: int, notification: NotificationUpdate, db: Session = Depends(get_db)):
    return update_notification(db=db, notification_id=notification_id, notification=notification)


def delete(notification_id: int, db: Session = Depends(get_db)):
    return delete_notification(db=db, notification_id=notification_id)
