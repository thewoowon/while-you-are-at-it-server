from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate, OrderResponse
from fastapi.responses import JSONResponse


def create_order(db: Session, order: OrderCreate, user_id: int, store_id: int, service_id: int):
    db_order = Order(**order.model_dump(), user_id=user_id,
                     store_id=store_id, service_id=service_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return OrderResponse.model_validate(db_order)


def update_order(db: Session, order: OrderUpdate, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.status = order.status if order.status else db_order.status
    db_order.payment_method = order.payment_method if order.payment_method else db_order.payment_method
    db_order.payment_status = order.payment_status if order.payment_status else db_order.payment_status
    db_order.delivery_date = order.delivery_date if order.delivery_date else db_order.delivery_date
    db_order.delivery_time = order.delivery_time if order.delivery_time else db_order.delivery_time
    db_order.delivery_address = order.delivery_address if order.delivery_address else db_order.delivery_address
    db_order.delivery_fee = order.delivery_fee if order.delivery_fee else db_order.delivery_fee
    db_order.total_price = order.total_price if order.total_price else db_order.total_price
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


def get_order_by_store_id(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return OrderResponse.model_validate(db_order)


def get_order_by_user_id(db: Session, user_id: int):
    db_orders = db.query(Order).filter(Order.user_id == user_id).all()
    if not db_orders:
        return []
    return [OrderResponse.model_validate(order) for order in db_orders]
