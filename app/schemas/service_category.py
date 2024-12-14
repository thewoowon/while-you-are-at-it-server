from pydantic import BaseModel


class ServiceCategoryBase(BaseModel):
    name: str
    address: str


class StoreCreate(ServiceCategoryBase):
    password: str


class StoreResponse(ServiceCategoryBase):
    id: int

    class Config:
        orm_mode = True
