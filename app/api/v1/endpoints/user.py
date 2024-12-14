from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user_service import create_user, get_user_by_id, update_user
from app.dependencies import get_db

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user
    """
    return create_user(db=db, user=user)


@router.get("/{user_id}", response_model=UserResponse)
def read(user_id: int, db: Session = Depends(get_db)):
    """
    Get user by ID
    """
    user = get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
def update(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    """
    Update user by ID
    """
    db_user = get_user_by_id(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user(db=db, user=user)


@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    """ 
    Delete user by ID
    """
    db_user = get_user_by_id(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
