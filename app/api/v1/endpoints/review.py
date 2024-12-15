# 리뷰 조회
# 리뷰 작성
# 리뷰 수정
# 리뷰 삭제
# 리뷰 좋아요
# 리뷰 좋아요 취소
# 리뷰 신고
# 리뷰 신고 취소
# 리뷰 신고 조회

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.review import ReviewCreate, ReviewResponse
from app.services.review_service import create_review, get_review_by_id, update_review
from app.dependencies import get_db

router = APIRouter()


def create(db: Session, store: ReviewCreate):
    return create_review(db=db, store=store)


def read(user_id: int, db: Session = Depends(get_db)):
    pass


def update(user_id: int, user: StoreUpdate, db: Session = Depends(get_db)):
    pass


def delete(user_id: int, db: Session = Depends(get_db)):
    pass
