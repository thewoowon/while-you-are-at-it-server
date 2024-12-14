# 아티클 생성
# 아티클 조회
# 아티클 수정
# 아티클 삭제

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.store import StoreCreate, StoreResponse
from app.services.store_service import create_store, get_store_by_id, update_store
from app.dependencies import get_db

router = APIRouter()


def create(db: Session, article: ArticleCreate):
    return create_store(db=db, article=article)


def read(user_id: int, db: Session = Depends(get_db)):
    pass


def update(user_id: int, user: ArticleUpdate, db: Session = Depends(get_db)):
    pass


def delete(user_id: int, db: Session = Depends(get_db)):
    pass
