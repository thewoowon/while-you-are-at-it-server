from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    # 기본 정보
    # 회원가입 시 필수
    name: str
    nickname: Optional[str] = None
    # 회원가입 시 필수
    email: str
    # 회원가입 시 필수
    phone_number: str
    address: Optional[str] = None
    src: Optional[str] = None


class UserCreate(UserBase):
    # 그대로 상속
    # 패스워드 필요 없음
    pass


class UserUpdate(BaseModel):
    # 업데이트 가능 필드만 Optional로 정의
    nickname: Optional[str] = None
    address: Optional[str] = None
    src: Optional[str] = None


class UserResponse(UserBase):
    # 응답에 id 추가
    id: int

    class Config:
        orm_mode = True
