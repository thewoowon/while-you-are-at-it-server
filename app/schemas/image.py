from pydantic import BaseModel


class ImageBase(BaseModel):
    name: str
    address: str


class ImageCreate(ImageBase):
    password: str


class ImageResponse(ImageBase):
    id: int

    class Config:
        orm_mode = True
