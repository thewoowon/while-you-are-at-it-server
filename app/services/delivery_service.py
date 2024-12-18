from fastapi import HTTPException
from app.schemas.delivery import DeliveryCreate, DeliveryUpdate, DeliveryResponse
from app.models.delivery import Delivery
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse


def create_delivery(db: Session, delivery: DeliveryCreate, user_id: int, article_id: int):
    db_delivery = Delivery(
        request_date=delivery.request_date,
        request_time=delivery.request_time,
        user_id=user_id,
        article_id=article_id
    )
    db.add(db_delivery)
    db.commit()
    db.refresh(db_delivery)
    return DeliveryResponse.model_validate(db_delivery)


def update_delivery(db: Session, delivery: DeliveryUpdate, delivery_id: int):
    db_delivery = db.query(Delivery).filter(Delivery.id == delivery_id).first()
    db_delivery.request_date = delivery.request_date if delivery.request_date else db_delivery.request_date
    db_delivery.request_time = delivery.request_time if delivery.request_time else db_delivery.request_time
    db.commit()
    db.refresh(db_delivery)
    return DeliveryResponse.model_validate(db_delivery)


def delete_delivery(db: Session, delivery_id: int):
    db_delivery = db.query(Delivery).filter(Delivery.id == delivery_id).first()
    if not db_delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    db.delete(db_delivery)
    db.commit()
    return JSONResponse(content={"message": "Delivery deleted successfully"}, status_code=200)


def get_delivery_by_id(db: Session, delivery_id: int):
    delivery = db.query(Delivery).filter(Delivery.id == delivery_id).first()
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return DeliveryResponse.model_validate(delivery)


def get_delivery_by_user_id(db: Session, user_id: int):
    deliveries = db.query(Delivery).filter(Delivery.user_id == user_id).all()
    if not deliveries:
        return []
    return [DeliveryResponse.model_validate(delivery) for delivery in deliveries]
