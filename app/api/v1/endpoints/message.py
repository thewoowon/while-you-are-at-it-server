from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.message import MessageCreate, MessageUpdate, MessageResponse
from app.services.message_service import create_message, get_message_by_chat_id, get_message_by_id, update_message
from app.dependencies import get_db

router = APIRouter()


def create(db: Session, store: MessageCreate):
    return create_message(db=db, store=store)


@router.get("/{chat_id}")
def read_all(chat_id: int, db: Session = Depends(get_db)):
    return get_message_by_chat_id(db, chat_id)


@router.get("/{message_id}")
def read_one(message_id: int, db: Session = Depends(get_db)):
    return get_message_by_id(db, message_id)


@router.put("/{message_id}")
def update(message_id: int, message: MessageUpdate, db: Session = Depends(get_db)):
    db_message = get_message_by_id(db, message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return update_message(db, message)


def delete(user_id: int, db: Session = Depends(get_db)):
    db_message = get_message_by_id(db, user_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    db.delete(db_message)
    db.commit()
    return {"message": "Message deleted successfully"}
