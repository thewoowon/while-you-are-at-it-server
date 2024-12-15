# 주문 생성
# 주문 조회
# 주문 취소
# 주문 수정
# 주문 상태 변경
# 주문 목록 조회

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.order import OrderCreate, OrderUpdate, OrderResponse
from app.services.order_service import create_order, get_order_by_id, update_order
from app.dependencies import get_db

router = APIRouter()


def create(db: Session, store: OrderCreate):
    return create_order(db=db, store=store)


def read(user_id: int, db: Session = Depends(get_db)):
    pass


@router.get("/{order_id}", response_model=OrderResponse)
def update(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    pass


def delete(user_id: int, db: Session = Depends(get_db)):
    pass
