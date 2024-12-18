from pydantic import BaseModel


class ServiceCategoryBase(BaseModel):
    code: str
    name: str


class ServiceCategoryCreate(ServiceCategoryBase):
    pass


class ServiceCategoryUpdate(ServiceCategoryBase):
    pass


class ServiceCategoryResponse(ServiceCategoryBase):
    id: int

    class Config:
        from_attributes = True
