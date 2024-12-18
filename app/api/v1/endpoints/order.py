# 주문 생성
# 주문 조회
# 주문 취소
# 주문 수정
# 주문 상태 변경
# 주문 목록 조회

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.order import OrderCreate, OrderUpdate, OrderResponse
from app.services.order_service import create_order, get_order_by_id, get_order_by_store_id, get_order_by_user_id, update_order, delete_order
from app.dependencies import get_db
from app.core.security import get_current_user
from typing import List

router = APIRouter()


@router.post("/", response_model=OrderResponse)
def create(order: OrderCreate, store_id: int, article_id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return create_order(db=db, order=order, user_id=user_id, store_id=store_id, article_id=article_id)


@router.get("/{order_id}", response_model=OrderResponse)
def read_one(order_id: int, db: Session = Depends(get_db)):
    return get_order_by_id(db=db, order_id=order_id)


@router.get("/", response_model=List[OrderResponse])
def read_all(store_id: int, db: Session = Depends(get_db)):
    return get_order_by_store_id(db=db, store_id=store_id)


@router.get("/", response_model=List[OrderResponse])
def read_my(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_order_by_user_id(db=db, user_id=user_id)


@router.get("/{order_id}", response_model=OrderResponse)
def update(order: OrderUpdate, order_id: int, db: Session = Depends(get_db)):
    return update_order(db=db, order_id=order_id, order=order)


@router.delete("/")
def delete(order_id: int, db: Session = Depends(get_db)):
    return delete_order(db=db, order_id=order_id)
