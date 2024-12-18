from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.image import ImageCreate
from app.models.image import Image
from fastapi.responses import JSONResponse


def create_image(order_id: int, image: ImageCreate, db: Session):
    db_image = Image(
        url=image.url,
        image_type=image.image_type,
        order_id=order_id
    )
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return ImageCreate.model_validate(db_image)


def delete_image(image_id: int, db: Session):
    db_image = db.query(Image).filter(Image.id == image_id).first()
    if not db_image:
        raise HTTPException(status_code=404, detail="Image not found")
    db.delete(db_image)
    db.commit()
    return JSONResponse(content={"message": "Image deleted successfully"}, status_code=200)


def get_image_by_id(image_id, db: Session):
    db_image = db.query(Image).filter(Image.id == image_id).first()
    if not db_image:
        raise HTTPException(status_code=404, detail="Image not found")
    return ImageCreate.model_validate(db_image)


def get_image_by_order_id(order_id: int, db: Session):
    images = db.query(Image).filter(Image.order_id == order_id).all()
    if not images:
        return []
    return [ImageCreate.model_validate(image) for image in images]
