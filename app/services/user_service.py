from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserResponse

# nickname, address, src -> Optional


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


def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.nickname = user.nickname
    db_user.address = user.address
    db_user.src = user.src
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
# Compare this snippet from app/api/v1/endpoints/user.py:
