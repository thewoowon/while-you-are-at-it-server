
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import requests


def google_auth(access_token: str):
    response = requests.get(
        "https://www.googleapis.com/oauth2/v1/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid token")
    user_info = response.json()
    return JSONResponse(content={"user": user_info}, status_code=200)


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
