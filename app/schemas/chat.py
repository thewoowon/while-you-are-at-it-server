from pydantic import BaseModel


class ChatBase(BaseModel):
    pass


class ChatCreate(ChatBase):
    pass


class ChatResponse(ChatBase):
    id: int

    class Config:
        orm_mode = True
