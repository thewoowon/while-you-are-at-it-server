from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.schemas.message import MessageCreate, MessageResponse, MessageUpdate
from app.models.message import Message
from fastapi.responses import JSONResponse


def create_message(db: Session, message: MessageCreate, chat_id: int, user_id: int):
    db_message = Message(
        message=message.message,
        sequence=message.sequence,
        chat_id=chat_id,
        user_id=user_id
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return MessageResponse.model_validate(db_message)


def update_message(db: Session, message: MessageUpdate, message_id: int):
    db_message = db.query(Message).filter(Message.id == message_id).first()
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    db_message.message = message.message if message.message else db_message.message
    db_message
    db.commit()
    db.refresh(db_message)
    return MessageResponse.model_validate(db_message)


def delete_message(db: Session, message_id: int):
    db_message = db.query(Message).filter(Message.id == message_id).first()
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    db.delete(db_message)
    db.commit()
    return JSONResponse(content={"message": "Message deleted successfully"}, status_code=200)


def get_message_by_chat_id(db: Session, chats_id: int):
    db_messages = db.query(Message).filter(Message.chat_id == chats_id).all()
    if not db_messages:
        return []
    return [MessageResponse.model_validate(message) for message in db_messages]


def get_message_by_id(db: Session, message_id: int):
    db_message = db.query(Message).filter(Message.id == message_id).first()
    if not db_message:
        return HTTPException(status_code=404, detail="Message not found")
    return MessageResponse.model_validate(db_message)
