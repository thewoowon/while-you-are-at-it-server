from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.image import ImageCreate, ImageResponse
from app.services.image_service import create_image, get_image_by_id, update_image, delete_image
from app.dependencies import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=ImageResponse)
def create(image: ImageCreate, db: Session = Depends(get_db),):
    return create_image(db=db, image=image)


@router.get("/", response_model=List[ImageResponse])
def read_all(db: Session = Depends(get_db)):
    return


@router.get("/{image_id}", response_model=ImageResponse)
def read_one(image_id: int, db: Session = Depends(get_db)):
    pass


@router.put("/{image_id}")
def delete(user_id: int, db: Session = Depends(get_db)):

    return {"message": "Image deleted successfully"}
