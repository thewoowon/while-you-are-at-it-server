
from fastapi import APIRouter
from app.services.auth_service import google_auth, naver_auth, kakao_auth

router = APIRouter()


@router.post("/google")
def google(access_token: str):
    return google_auth(access_token)


@router.post("/naver")
def naver(access_token: str):
    return naver_auth(access_token)


@router.post("/kakao")
def kakao(access_token: str):
    return kakao_auth(access_token)
