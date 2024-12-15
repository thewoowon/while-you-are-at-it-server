from pydantic import BaseModel


class ImageBase(BaseModel):
    url: str
    image_type: str


class ImageCreate(ImageBase):
    pass


class ImageResponse(ImageBase):
    id: int

    class Config:
        orm_mode = True
