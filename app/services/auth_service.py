
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.services.user_service import create_user
from app.core.security import decode_token
import requests
import jwt
from datetime import datetime, timedelta, timezone
from settings import (
    DEFAULT_PROFILE_PIC,
    GOOGLE_TOKEN_INFO_URL,
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_DAYS,
)
from app.models.user import User
from app.schemas.user import UserCreate
from app.models.token import Token


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY,
                             algorithm=JWT_ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY,
                             algorithm=JWT_ALGORITHM)
    return encoded_jwt


async def google_auth(request: Request, db: Session):
    try:
        data = await request.json()
        id_token = data.get("id_token")
        is_auto_login = data.get("is_selected")

        if not id_token:
            raise HTTPException(status_code=400, detail="ID token is required")

        # Google 서버에 idToken 검증 요청
        try:
            response = requests.get(GOOGLE_TOKEN_INFO_URL, params={
                                    "id_token": id_token})
            response.raise_for_status()  # HTTP 에러 처리
        except requests.RequestException as e:
            raise HTTPException(
                status_code=400, detail=f"Failed to verify token: {str(e)}")

        # 2. 검증 결과 확인
        token_info = response.json()
        email = token_info.get("email")

        if not email:
            raise HTTPException(
                status_code=400, detail="Email is missing in token")

        # 사용자 조회 또는 생성
        user = db.query(User).filter(User.email == email).first()

        if not user:
            # 새로운 사용자 생성
            user = create_user(
                db=db,
                user=UserCreate(
                    name=token_info.get("name", "Unknown"),
                    nickname="",
                    email=email,
                    phone_number="",
                    address="",
                    src=DEFAULT_PROFILE_PIC,
                    is_auto_login=is_auto_login,
                ),
            )

        # 토큰 생성
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

        access_token = create_access_token(
            data={"sub": user.email, "user_id": user.id}, expires_delta=access_token_expires
        )
        refresh_token = create_refresh_token(
            data={"sub": user.email, "user_id": user.id}, expires_delta=refresh_token_expires
        )

        # 사용자 데이터 및 토큰 반환
        user_data = {
            "id": user.id,
            "name": user.name,
            "nickname": user.nickname,
            "email": user.email,
            "phone_number": user.phone_number,
            "address": user.address,
            "src": user.src,
        }

        return JSONResponse(
            content={
                "user": user_data,
                "access_token": access_token,
                "refresh_token": refresh_token,
            },
            status_code=200,
        )
    except Exception as e:
        print("Error:", e)
        print("Failed to verify token")
        raise HTTPException(status_code=400, detail="Invalid token")


def naver_auth(access_token: str):
    response = requests.get(
        "https://openapi.naver.com/v1/nid/me",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid token")
    user_info = response.json()
    return JSONResponse(content={"user": user_info}, status_code=200)


def kakao_auth(access_token: str):
    response = requests.get(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid token")
    user_info = response.json()
    return JSONResponse(content={"user": user_info}, status_code=200)


def refresh_token_func(request: Request, db: Session):
    try:
        # 1. Refresh Token 디코딩 및 검증 -> 토큰이 유효하지 않거나 만료된 경우 예외 발생
        payload = decode_token(request.refresh_token)
        user_id = payload.get("user_id")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )

        # token과 user_id를 이용하여 DB에서 refresh_token 조회
        token_obj = db.query(Token).filter(
            Token.user_id == user_id and Token.refresh_token == request.refresh_token).first()

        if not token_obj:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )

        if not token_obj.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Inactive refresh token"
            )

        # 2. 새로운 Access Token 발급
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"user_id": user_id}, expires_delta=access_token_expires
        )

        return JSONResponse(content={"access_token": access_token}, status_code=200)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token"
        )
