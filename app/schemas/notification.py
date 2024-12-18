from pydantic import BaseModel


class NotificationBase(BaseModel):
    title: str
    contents: str
    notification_type: str
    status: str


class NotificationCreate(NotificationBase):
    pass


class NotificationUpdate(BaseModel):
    status: str


class NotificationResponse(NotificationBase):
    id: int

    class Config:
        from_attributes = True
