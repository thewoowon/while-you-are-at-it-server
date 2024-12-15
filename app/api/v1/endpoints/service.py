# 서비스 등록
# 서비스 조회
# 서비스 수정
# 서비스 삭제
# 서비스 리스트 조회
# 서비스 상세 조회

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.service import ServiceCreate, ServiceUpdate, ServiceResponse
from app.services.service_service import create_service, get_service_by_id, update_service
from app.dependencies import get_db

router = APIRouter()


def create(db: Session, store: ServiceCreate):
    return create_service(db=db, store=store)


def read(user_id: int, db: Session = Depends(get_db)):
    pass


def update(user_id: int, user: ServiceUpdate, db: Session = Depends(get_db)):
    pass


def delete(user_id: int, db: Session = Depends(get_db)):
    pass
