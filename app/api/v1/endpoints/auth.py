
from fastapi import APIRouter, Request, Depends
from app.services.auth_service import google_auth, naver_auth, kakao_auth
from app.schemas.auth import AuthRequest
from app.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/google")
async def google(request: Request, db: Session = Depends(get_db),):
    return await google_auth(request, db)


@router.post("/naver")
def naver(access_token: str):
    return naver_auth(access_token)


@router.post("/kakao")
def kakao(access_token: str):
    return kakao_auth(access_token)
