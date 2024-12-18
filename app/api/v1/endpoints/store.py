# 가게 등록/생성
# 가게 정보 수정
# 가게 서비스 등록
# 가게 서비스 수정
# 가게 서비스 삭제
# 가게 서비스 조회

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.store import StoreCreate, StoreUpdate, StoreResponse
from app.services.store_service import create_store, get_store_by_id, update_store, delete_store
from app.dependencies import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=StoreResponse)
def create(store: StoreCreate, db: Session = Depends(get_db)):
    return create_store(db=db, store=store)


@router.get("/{store_id}", response_model=StoreResponse)
def read_one(store_id: int, db: Session = Depends(get_db)):
    return get_store_by_id(db=db, store_id=store_id)


@router.get("/", response_model=List[StoreResponse])
def update(store_id: int, store: StoreUpdate, db: Session = Depends(get_db)):
    return update_store(db=db, store_id=store_id, store=store)


@router.delete("/{store_id}")
def delete(store_id: int, db: Session = Depends(get_db)):
    return delete_store(db=db, store_id=store_id)
