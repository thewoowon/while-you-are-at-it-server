from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate, OrderResponse
from fastapi.responses import JSONResponse


def create_order(db: Session, order: OrderCreate, user_id: int, store_id: int, service_id: int):
    db_order = Order(
        description=order.description,
        order_type=order.order_type,
        user_id=user_id,
        store_id=store_id, service_id=service_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return OrderResponse.model_validate(db_order)


def update_order(db: Session, order: OrderUpdate, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.description = order.description if order.description else db_order.description
    db_order.order_type = order.order_type if order.order_type else db_order.order_type
    db.commit()
    db.refresh(db_order)
    return OrderResponse.model_validate(db_order)


def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return JSONResponse(content={"message": "Order deleted successfully"}, status_code=200)


def get_order_by_id(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return OrderResponse.model_validate(db_order)


def get_order_by_store_id(db: Session, store_id: int):
    db_order = db.query(Order).filter(Order.store_id == store_id).all()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return OrderResponse.model_validate(db_order)


def get_order_by_user_id(db: Session, user_id: int):
    db_orders = db.query(Order).filter(Order.user_id == user_id).all()
    if not db_orders:
        return []
    return [OrderResponse.model_validate(order) for order in db_orders]
