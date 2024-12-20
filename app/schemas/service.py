from pydantic import BaseModel
from typing import Optional


class ServiceBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    unit: Optional[str] = None
    price: Optional[str] = None
    discount_rate: Optional[str] = None
    service_type: Optional[str] = None


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(ServiceBase):
    pass


class ServiceResponse(ServiceBase):
    id: int

    class Config:
        from_attributes = True
