from pydantic import BaseModel
from typing import Optional


class OrderBase(BaseModel):
    description: str
    order_type: str


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    description: Optional[str] = None
    order_type: Optional[str] = None


class OrderResponse(OrderBase):
    id: int

    class Config:
        from_attributes = True
