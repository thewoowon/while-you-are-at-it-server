from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.message import MessageCreate, MessageUpdate, MessageResponse
from app.services.message_service import create_message, get_message_by_chat_id, get_message_by_id, update_message, delete_message
from app.dependencies import get_db
from typing import List

router = APIRouter()


@router.post("/", response_model=MessageResponse)
def create(message: MessageCreate, chat_id: int, user_id: int = Depends(get_db), db: Session = Depends(get_db)):
    return create_message(db=db, message=message, chat_id=chat_id, user_id=user_id,)


@router.get("/{chat_id}", response_model=List[MessageResponse])
def read_all(chat_id: int, db: Session = Depends(get_db)):
    return get_message_by_chat_id(db=db, chat_id=chat_id)


@router.get("/{message_id}", response_model=MessageResponse)
def read_one(message_id: int, db: Session = Depends(get_db)):
    return get_message_by_id(db=db, message_id=message_id)


@router.put("/{message_id}", response_model=MessageResponse)
def update(message_id: int, message: MessageUpdate, db: Session = Depends(get_db)):
    return update_message(db=db, message_id=message_id, message=message)


@router.delete("/{message_id}")
def delete(message_id: int, db: Session = Depends(get_db)):
    return delete_message(db=db, message_id=message_id)
