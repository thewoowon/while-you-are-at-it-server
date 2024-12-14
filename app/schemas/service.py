from pydantic import BaseModel


class ServiceBase(BaseModel):
    name: str
    address: str


class ServiceCreate(ServiceBase):
    password: str


class ServiceResponse(ServiceBase):
    id: int

    class Config:
        orm_mode = True
