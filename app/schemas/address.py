from pydantic import BaseModel
from typing import Optional


class AddressBase(BaseModel):
    address_string: str
    postal_code: str
    latitude: str
    longitude: str
