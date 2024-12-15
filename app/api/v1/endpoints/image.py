from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.image import ImageCreate, ImageResponse
from app.services.image_service import create_image, get_image_by_id
from app.dependencies import get_db

router = APIRouter()


@router.post("/", response_model=ImageResponse)
def create(db: Session, image: ImageCreate):
    return create_image(db=db, image=image)


@router.get("/", response_model=ImageResponse)
def read_all(db: Session = Depends(get_db)):
    pass


@router.get("/{image_id}", response_model=ImageResponse)
def read_one(image_id: int, db: Session = Depends(get_db)):
    pass


@router.put("/{image_id}", response_model=ImageResponse)
def delete(user_id: int, db: Session = Depends(get_db)):
    db_image = get_image_by_id(db, user_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    db.delete(db_image)
    db.commit()
    return {"message": "Image deleted successfully"}
