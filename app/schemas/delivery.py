from pydantic import BaseModel
from typing import Optional


class DeliveryBase(BaseModel):
    request_date: str
    request_time: str


class DeliveryCreate(DeliveryBase):
    pass


class DeliveryUpdate(BaseModel):
    request_date: Optional[str] = None
    request_time: Optional[str] = None


class DeliveryResponse(DeliveryBase):
    id: int

    class Config:
        from_attributes = True
