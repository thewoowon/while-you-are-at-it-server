from pydantic import BaseModel
from typing import Optional


class StoreBase(BaseModel):
    name: str
    address: Optional[str] = None
    store_type: Optional[str] = None
    business_hours: Optional[str] = None
    phone_number: Optional[str] = None


class StoreCreate(StoreBase):
    pass


class StoreUpdate(StoreBase):
    name: Optional[str] = None
    address: Optional[str] = None
    store_type: Optional[str] = None
    business_hours: Optional[str] = None
    phone_number: Optional[str] = None


class StoreResponse(StoreBase):
    id: int

    class Config:
        orm_mode = True
