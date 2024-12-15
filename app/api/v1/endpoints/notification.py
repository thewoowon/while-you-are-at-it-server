# 알림 생성
# 알림 조회
# 알림 삭제
# 알림 수정
# 알림 읽음 처리

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.notification import NotificationCreate, NotificationResponse
from app.services.notification_service import create_notification, get_notification_by_id, update_notification
from app.dependencies import get_db

router = APIRouter()


def create(db: Session, store: NotificationCreate):
    return create_notification(db=db, store=store)


def read(user_id: int, db: Session = Depends(get_db)):
    pass


def delete(user_id: int, db: Session = Depends(get_db)):
    pass
