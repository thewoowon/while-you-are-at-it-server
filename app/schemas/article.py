from pydantic import BaseModel
from typing import Optional
from app.schemas.address import AddressBase


class ArticleBase(BaseModel):
    title: str
    contents: str
    article_type: str
    pick_up_location: str
    pick_up_time: str
    destination: str
    departure_date_and_time: str
    number_of_recruits: str
    process_status: str


# access_token으로 user_id를 찾기 위한 클래스
class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    contents: Optional[str] = None
    article_type: Optional[str] = None
    pick_up_location: Optional[str] = None
    pick_up_time: Optional[str] = None
    destination: Optional[str] = None
    departure_date_and_time: Optional[str] = None
    number_of_recruits: Optional[str] = None
    process_status: Optional[str] = None


class ArticleResponse(ArticleBase):
    id: int
    address: Optional[AddressBase]

    class Config:
        from_attributes = True
