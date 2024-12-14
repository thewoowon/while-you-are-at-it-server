from pydantic import BaseModel


class MessageBase(BaseModel):
    name: str
    address: str


class MessageCreate(MessageBase):
    password: str


class MessageResponse(MessageBase):
    id: int

    class Config:
        orm_mode = True
