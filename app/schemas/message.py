from pydantic import BaseModel


class MessageBase(BaseModel):
    message: str
    sequence: str


class MessageCreate(MessageBase):
    pass


class MessageUpdate(MessageBase):
    message: str


class MessageResponse(MessageBase):
    id: int

    class Config:
        from_attributes = True
