from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.chat import ChatCreate, ChatResponse
from app.services.chat_service import create_chat, get_chat_by_id, get_chat_by_user_id
from app.dependencies import get_db
from core.security import get_current_user

router = APIRouter()


@router.post("/", response_model=ChatResponse)
def create(db: Session, chat: ChatCreate):
    return create_chat(db=db, chat=chat)


@router.get("/", response_model=ChatResponse)
def read_all(user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_chat_by_user_id(db=db, user_id=user_id)


@router.get("/{chat_id}", response_model=ChatResponse)
def read_one(chat_id: int, db: Session = Depends(get_db)):
    return get_chat_by_id(db=db, chat_id=chat_id)


@router.put("/{chat_id}", response_model=ChatResponse)
def delete(chat_id: int, db: Session = Depends(get_db)):
    db_chat = get_chat_by_id(db=db, chat_id=chat_id)
    if not db_chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    db.delete(db_chat)
    db.commit()
    return {"message": "Chat deleted successfully"}
