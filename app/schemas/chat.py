from pydantic import BaseModel


class ChatBase(BaseModel):
    name: str
    address: str


class ChatCreate(ChatBase):
    password: str


class ChatResponse(ChatBase):
    id: int

    class Config:
        orm_mode = True
