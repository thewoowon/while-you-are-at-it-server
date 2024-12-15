# 카테고리 조회

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.service_category import ServiceCategoryCreate, ServiceCategoryUpdate, ServiceCategoryResponse
from app.services.service_category_service import create_service_category, get_service_category_by_id, update_service_category
from app.dependencies import get_db

router = APIRouter()


def create(db: Session, store: ServiceCategoryCreate):
    return create_service_category(db=db, store=store)


def read(user_id: int, db: Session = Depends(get_db)):
    pass


def update(user_id: int, user: ServiceCategoryUpdate, db: Session = Depends(get_db)):
    pass


def delete(user_id: int, db: Session = Depends(get_db)):
    pass
