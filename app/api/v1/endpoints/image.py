# 이미지 생성
# 이미지 업로드
# 이미지 삭제
# 이미지 수정
# 이미지 조회
# 이미지 리스트 조회
# 이미지 좋아요
# 이미지 좋아요 취소
# 이미지 댓글 생성
# 이미지 댓글 삭제
# 이미지 댓글 수정
# 이미지 댓글 조회
# 이미지 댓글 리스트 조회

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
