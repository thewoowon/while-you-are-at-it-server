from pydantic import BaseModel


class ReviewBase(BaseModel):
    name: str
    address: str


class ReviewCreate(ReviewBase):
    password: str


class ReviewResponse(ReviewBase):
    id: int

    class Config:
        orm_mode = True
