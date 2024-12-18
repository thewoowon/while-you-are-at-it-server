from pydantic import BaseModel
from typing import Optional


class ReviewBase(BaseModel):
    title: str
    contents: str
    score: str


class ReviewCreate(ReviewBase):
    store_id: int


class ReviewUpdate(BaseModel):
    title: Optional[str] = None
    contents: Optional[str] = None
    score: Optional[str] = None


class ReviewResponse(ReviewBase):
    id: int

    class Config:
        from_attributes = True
