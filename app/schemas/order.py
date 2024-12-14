from pydantic import BaseModel


class OrderBase(BaseModel):
    name: str
    address: str


class OrderCreate(OrderBase):
    password: str


class OrderResponse(OrderBase):
    id: int

    class Config:
        orm_mode = True
