# core/security.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def decode_token(token: str):
    # JWT 디코딩 로직 (예: PyJWT 사용)
    # 토큰에서 user_id를 추출하는 함수
    # 여기에 토큰 유효성 검사 포함
    return {"user_id": "example_user_id"}  # 예시: 디코딩 후 반환값


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_token(token)
    if not payload or "user_id" not in payload:
        raise credentials_exception
    return payload["user_id"]
