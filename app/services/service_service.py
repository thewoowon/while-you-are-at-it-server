from sqlalchemy.orm import Session
from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceUpdate
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def create_service(db: Session, store_id: int, service: ServiceCreate):
    db_service = Service(
        name=service.name,
        description=service.description,
        unit=service.unit,
        price=service.price,
        discount_rate=service.discount_rate,
        service_type=service.service_type,
        store_id=store_id
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service


def update_service(db: Session, service_id: int, service: ServiceUpdate):
    db_service = db.query(Service).filter(Service.id == service_id).first()
    if not db_service:
        raise HTTPException(status_code=404, detail="Service not found")
    db_service.name = service.name if service.name else db_service.name
    db_service.description = service.description if service.description else db_service.description
    db_service.unit = service.unit if service.unit else db_service.unit
    db_service.price = service.price if service.price else db_service.price
    db_service.discount_rate = service.discount_rate if service.discount_rate else db_service.discount_rate
    db_service.service_type = service.service_type if service.service_type else db_service.service_type
    db.commit()
    db.refresh(db_service)
    return db_service


def delete_service(db: Session, service_id: int):
    db_service = db.query(Service).filter(Service.id == service_id).first()
    if not db_service:
        raise HTTPException(status_code=404, detail="Service not found")
    db.delete(db_service)
    db.commit()
    return JSONResponse(content={"message": "Service deleted successfully"}, status_code=200)


def get_service_by_id(db: Session, service_id: int):
    db_service = db.query(Service).filter(Service.id == service_id).first()
    if not db_service:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service


def get_service_by_store_id(db: Session, store_id: int):
    db_service = db.query(Service).filter(Service.store_id == store_id).all()
    if not db_service:
        return []
    return db_service
