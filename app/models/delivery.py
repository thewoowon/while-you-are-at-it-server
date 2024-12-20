from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Delivery 클래스
class Delivery(Base):
    __tablename__ = "delivery"

    request_date = Column(String, nullable=False)
    request_time = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    article_id = Column(Integer, ForeignKey("article.id", ondelete="CASCADE"))

    # 관계 설정
    user = relationship("User")
    article = relationship("Article")
