from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.delivery import DeliveryCreate, DeliveryUpdate, DeliveryResponse
from app.services.delivery_service import create_delivery, get_delivery_by_id, get_delivery_by_user_id, update_delivery
from app.dependencies import get_db
from core.security import get_current_user


router = APIRouter()


@router.post("/", response_model=DeliveryResponse)
def create(db: Session, delivery: DeliveryCreate):
    return create_delivery(db=db, delivery=delivery)


@router.get("/", response_model=DeliveryResponse)
def read_all(user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_delivery_by_user_id(db=db, user_id=user_id)


@router.get("/{delivery_id}", response_model=DeliveryResponse)
def read_one(delivery_id: int, db: Session = Depends(get_db)):
    return get_delivery_by_id(db=db, delivery_id=delivery_id)


@router.put("/{delivery_id}", response_model=DeliveryResponse)
def update(delivery_id: int, delivery: DeliveryUpdate, db: Session = Depends(get_db)):
    db_delivery = get_delivery_by_id(db=db, delivery_id=delivery_id)
    if not db_delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return update_delivery(db=db, delivery=delivery)


@router.delete("/{delivery_id}")
def delete(delivery_id: int, db: Session = Depends(get_db)):
    db_delivery = get_delivery_by_id(db=db, delivery_id=delivery_id)
    if not db_delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    db.delete(db_delivery)
    db.commit()
    return {"message": "Delivery deleted successfully"}
