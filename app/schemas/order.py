from pydantic import BaseModel


class OrderBase(BaseModel):
    description: str
    order_type: str


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int

    class Config:
        from_attributes = True
