from pydantic import BaseModel


class DeliveryBase(BaseModel):
    request_date: str
    request_time: str


class DeliveryCreate(DeliveryBase):
    pass


class DeliveryUpdate(DeliveryBase):
    request_date: str
    request_time: str


class DeliveryResponse(DeliveryBase):
    id: int

    class Config:
        from_attributes = True
