from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.article import Article
from app.schemas.article import ArticleCreate, ArticleUpdate, ArticleResponse
from fastapi.responses import JSONResponse
from app.models.address import Address


def create_article(db: Session, user_id: str, article: ArticleCreate):
    db_article = Article(
        title=article.title,
        contents=article.contents,
        article_type=article.article_type,
        pick_up_location=article.pick_up_location,
        pick_up_time=article.pick_up_time,
        destination=article.destination,
        departure_date_and_time=article.departure_date_and_time,
        number_of_recruits=article.number_of_recruits,
        process_status=article.process_status,
        user_id=user_id
    )

    db.add(db_article)
    db.commit()
    db.refresh(db_article)

    # 역기서 address를 생성하고 article에 연결
    # 여기서 다음 카카오 검색

    db_address = Address(
        address_string=article.pick_up_location,
        postal_code="",
        latitude="",
        longitude="",
        article_id=db_article.id
    )

    return ArticleResponse.model_validate(db_article)


def update_article(db: Session, article_id: int, article: ArticleUpdate):

    db_article = db.query(Article).filter(Article.id == article_id).first()
    db_article.title = article.title if article.title else db_article.title
    db_article.contents = article.contents if article.contents else db_article.contents
    db_article.article_type = article.article_type if article.article_type else db_article.article_type
    db_article.pick_up_location = article.pick_up_location if article.pick_up_location else db_article.pick_up_location
    db_article.pick_up_time = article.pick_up_time if article.pick_up_time else db_article.pick_up_time
    db_article.destination = article.destination if article.destination else db_article.destination
    db_article.departure_date_and_time = article.departure_date_and_time if article.departure_date_and_time else db_article.departure_date_and_time
    db_article.number_of_recruits = article.number_of_recruits if article.number_of_recruits else db_article.number_of_recruits
    db_article.process_status = article.process_status if article.process_status else db_article.process_status

    db.commit()
    db.refresh(db_article)
    return db_article


def delete_article(db: Session, article_id: int):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    db.delete(db_article)
    db.commit()
    return JSONResponse(content={"message": "Article deleted successfully"}, status_code=200)


def get_article_by_id(db: Session, article_id: int):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return ArticleResponse.model_validate(article)


def get_article_by_user_id(db: Session, user_id: int):
    articles = db.query(Article).filter(Article.user_id == user_id).all()
    if not articles:
        return []
    return [ArticleResponse.model_validate(article) for article in articles]


def get_article_by_location(db: Session, location: list[str]):
    articles = db.query(Article).filter(
        Article.pick_up_location == location).all()
    if not articles:
        return []
    return [ArticleResponse.model_validate(article) for article in articles]
