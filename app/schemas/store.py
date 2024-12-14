from pydantic import BaseModel


class StoreBase(BaseModel):
    name: str
    address: str


class StoreCreate(StoreBase):
    password: str


class StoreResponse(StoreBase):
    id: int

    class Config:
        orm_mode = True
