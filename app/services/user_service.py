from fastapi import HTTPException, Request
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from fastapi.responses import JSONResponse


def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name,
                   nickname=user.nickname,
                   email=user.email,
                   phone_number=user.phone_number,
                   address=user.address,
                   src=user.src)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def update_user(db: Session, user_id: int, request: Request):

    context = await request.json()
    user = UserUpdate(**context)

    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.nickname = user.nickname
    db_user.address = user.address
    db_user.src = user.src
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return JSONResponse(content={"message": "User deleted successfully"}, status_code=200)


def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_user_by_nickname(db: Session, nickname: str):
    user = db.query(User).filter(User.nickname == nickname).first()
    if not user:
        return JSONResponse(content={
            "message": "Nickname is available", "is_available": True}, status_code=200)
    return JSONResponse(content={"message": "Nickname is already taken", "is_available": False}, status_code=200)


def get_user_by_email(db: Session, email: str):
    print("Email:", email)
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
# Compare this snippet from app/api/v1/endpoints/user.py:
