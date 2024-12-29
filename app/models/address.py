from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Address 클래스
class Address(Base):
    __tablename__ = "address"

    postal_code = Column(String, nullable=False)
    address_string = Column(String, nullable=False)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    article_id = Column(Integer, ForeignKey("article.id", ondelete="CASCADE"))

    # 관계 설정
    article = relationship("Article", back_populates="address")
