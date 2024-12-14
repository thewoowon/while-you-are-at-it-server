from pydantic import BaseModel


class DeliveryBase(BaseModel):
    name: str
    address: str


class DeliveryCreate(DeliveryBase):
    password: str


class DeliveryResponse(DeliveryBase):
    id: int

    class Config:
        orm_mode = True
