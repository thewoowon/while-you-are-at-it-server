from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.image import ImageCreate, ImageResponse
from app.services.image_service import create_image, get_image_by_id, delete_image, get_image_by_order_id
from app.dependencies import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=ImageResponse)
def create(order_id: int, image: ImageCreate, db: Session = Depends(get_db),):
    return create_image(order_id=order_id, image=image, db=db)


@router.get("/", response_model=List[ImageResponse])
def read_all(order_id: int, db: Session = Depends(get_db)):
    return get_image_by_order_id(db=db, order_id=order_id)


@router.get("/{image_id}", response_model=ImageResponse)
def read_one(image_id: int, db: Session = Depends(get_db)):
    return get_image_by_id(image_id=image_id, db=db)


@router.put("/{image_id}")
def delete(image_id: int, db: Session = Depends(get_db)):
    return delete_image(image_id=image_id, db=db)
