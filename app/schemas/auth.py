from pydantic import BaseModel
from typing import Optional


class AuthBase(BaseModel):
    pass


class AuthRequest(AuthBase):
    idToken: str
