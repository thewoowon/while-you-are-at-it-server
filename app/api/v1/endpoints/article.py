from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.article import ArticleCreate, ArticleUpdate, ArticleResponse
from app.services.article_service import create_article, get_article_by_id, get_article_by_location, get_article_by_user_id, update_article, delete_article
from app.dependencies import get_db
from app.core.security import get_current_user
from typing import List

router = APIRouter()


@router.get("/one", response_model=ArticleResponse)
def read_one(article_id: int, db: Session = Depends(get_db)):
    return get_article_by_id(db=db, article_id=article_id)


@router.get("/all", response_model=List[ArticleResponse])
def read_all(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_article_by_user_id(db=db, user_id=user_id)


@router.post("/", response_model=ArticleResponse)
def create(article: ArticleCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return create_article(db=db, article=article, user_id=user_id)


@router.put("/{article_id}", response_model=ArticleResponse)
def update(article: ArticleUpdate, article_id: int, db: Session = Depends(get_db)):
    return update_article(db=db, article_id=article_id, article=article)


@router.delete("/{article_id}")
def delete(article_id: int, db: Session = Depends(get_db)):
    return delete_article(db=db, article_id=article_id)
