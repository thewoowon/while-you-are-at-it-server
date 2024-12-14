from pydantic import BaseModel


class NotificationBase(BaseModel):
    name: str
    address: str


class NotificationCreate(NotificationBase):
    password: str


class NotificationResponse(NotificationBase):
    id: int

    class Config:
        orm_mode = True
