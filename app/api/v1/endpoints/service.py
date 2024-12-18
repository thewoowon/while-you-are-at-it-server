# 서비스 등록
# 서비스 조회
# 서비스 수정
# 서비스 삭제
# 서비스 리스트 조회
# 서비스 상세 조회

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.service import ServiceCreate, ServiceUpdate, ServiceResponse
from app.services.service_service import create_service, get_service_by_id, update_service, get_service_by_store_id, delete_service
from app.dependencies import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=ServiceResponse)
def create(store_id: int, service: ServiceCreate, db: Session = Depends(get_db)):
    return create_service(db=db, store_id=store_id, service=service)


@router.get("/{service_id}", response_model=ServiceResponse)
def read_one(service_id: int, db: Session = Depends(get_db)):
    return get_service_by_id(db=db, service_id=service_id)


@router.get("/", response_model=List[ServiceResponse])
def read_all(store_id: int, db: Session = Depends(get_db)):
    return get_service_by_store_id(db=db, store_id=store_id)


@router.put("/{service_id}", response_model=ServiceResponse)
def update(service_id: int, service: ServiceUpdate, db: Session = Depends(get_db)):
    return update_service(db=db, service_id=service_id, service=service)


@router.delete("/{service_id}")
def delete(service_id: int, db: Session = Depends(get_db)):
    return delete_service(db=db, service_id=service_id)
