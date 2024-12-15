from sqlalchemy.orm import Session
from app.models.article import Article
from app.schemas.article import ArticleCreate, ArticleUpdate, ArticleResponse


def create_article(db: Session, ):
    pass


def update_article(db: Session, ):
    pass


def delete_article(db: Session, ):
    pass


def get_article_by_id(db: Session, user_id: int):
    pass


def get_article_by_location(db: Session, article_id: int):
    pass
