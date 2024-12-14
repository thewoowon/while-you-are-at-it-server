# 알림 생성
# 알림 조회
# 알림 삭제
# 알림 수정
# 알림 읽음 처리

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.store import StoreCreate, StoreResponse
from app.services.store_service import create_store, get_store_by_id, update_store
from app.dependencies import get_db

router = APIRouter()


def create(db: Session, store: StoreCreate):
    return create_store(db=db, store=store)


def read(user_id: int, db: Session = Depends(get_db)):
    pass


def update(user_id: int, user: StoreUpdate, db: Session = Depends(get_db)):
    pass


def delete(user_id: int, db: Session = Depends(get_db)):
    pass
