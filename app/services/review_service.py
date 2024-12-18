from sqlalchemy.orm import Session
from app.models.review import Review
from app.schemas.review import ReviewCreate, ReviewUpdate
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def create_review(db: Session, review: ReviewCreate, user_id: int, store_id: int):
    db_review = Review(
        title=review.title,
        content=review.content,
        rating=review.rating,
        user_id=user_id,
        store_id=store_id
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def update_review(db: Session, review: ReviewUpdate, review_id: int):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    db_review.title = review.title if review.title else db_review.title
    db_review.contents = review.contents if review.contents else db_review.contents
    db_review.score = review.score if review.score else db_review.score
    db.commit()
    db.refresh(db_review)
    return db_review


def delete_review(db: Session, review_id: int):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    db.delete(db_review)
    db.commit()
    return JSONResponse(content={"message": "Review deleted successfully"}, status_code=200)


def get_review_by_id(db: Session, review_id: int):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review


def get_review_by_user_id(db: Session, user_id: int):
    reviews = db.query(Review).filter(Review.user_id == user_id).all()
    if not reviews:
        return []
    return reviews


def get_review_by_store_id(db: Session, store_id: int):
    reviews = db.query(Review).filter(Review.store_id == store_id).all()
    if not reviews:
        return []
    return reviews
