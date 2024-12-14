# 채팅 생성
# 채팅 조회
# 채팅 수정
# 채팅 삭제

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.chat import ChatCreate, ChatUpdate, ChatResponse
from app.services.chat_service import create_chat, get_chat_by_id, update_chat
from app.dependencies import get_db

router = APIRouter()


def create(db: Session, store: ChatCreate):
    return create_chat(db=db, store=store)


def read(user_id: int, db: Session = Depends(get_db)):
    pass


def update(user_id: int, user: ChatUpdate, db: Session = Depends(get_db)):
    pass


def delete(user_id: int, db: Session = Depends(get_db)):
    pass
