from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user_service import create_user, get_user_by_id, update_user, get_user_by_nickname, delete_user
from app.dependencies import get_db
from app.core.security import get_current_user

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user
    """
    return create_user(db=db, user=user)


@router.get("/me", response_model=UserResponse)
def read(user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Get user by ID
    """
    return get_user_by_id(db=db, user_id=user_id)

# nickname 중복체크


@router.get("/nickname/{nickname}")
def check_nickname(nickname: str, db: Session = Depends(get_db)):
    """
    Check if the nickname is already taken
    """
    return get_user_by_nickname(db=db, nickname=nickname)


# user_id: str = Depends(get_current_user),
@router.put("/me", response_model=UserResponse)
async def update(request: Request, db: Session = Depends(get_db)):
    """
    Update user by ID
    """
    return await update_user(db=db, user_id=1, request=request)


@router.delete("/me")
def delete(user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    """ 
    Delete user by ID
    """
    return delete_user(db=db, user_id=user_id)
