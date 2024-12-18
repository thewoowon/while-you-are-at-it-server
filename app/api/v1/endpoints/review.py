from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.review import ReviewCreate, ReviewUpdate, ReviewResponse
from app.services.review_service import create_review, get_review_by_id, update_review, get_review_by_user_id, get_review_by_store_id, delete_review
from app.dependencies import get_db
from app.core.security import get_current_user
from typing import List

router = APIRouter()


@router.post("/", response_model=ReviewResponse)
def create(review: ReviewCreate, store_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return create_review(db=db, review=review, store_id=store_id, user_id=user_id)


@router.get("/{review_id}", response_model=ReviewResponse)
def read_one(review_id: int, db: Session = Depends(get_db)):
    return get_review_by_id(db=db, review_id=review_id)


@router.get("/my", response_model=List[ReviewResponse])
def read_my(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_review_by_user_id(db=db, user_id=user_id)


@router.get("/store/{store_id}", response_model=List[ReviewResponse])
def read_all(store_id: int, db: Session = Depends(get_db)):
    return get_review_by_store_id(db=db, store_id=store_id)


@router.put("/{review_id}", response_model=ReviewResponse)
def update(review: ReviewUpdate, db: Session = Depends(get_db), user_id: str = Depends(get_current_user),):
    update_review(db=db, review=review, user_id=user_id, )


@router.delete("/{review_id}")
def delete(review_id: int, db: Session = Depends(get_db)):
    return delete_review(db=db, review_id=review_id)
