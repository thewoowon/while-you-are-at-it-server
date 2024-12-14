from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# User 클래스 -> 대부분 모든 객체가 User 클래스를 사용
class User(Base):
    __tablename__ = "user"

    name = Column(String, nullable=False)
    nickname = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=True)
    src = Column(String, nullable=True)

    # 관계 설정
    articles = relationship("Article", back_populates="user")
    chats = relationship("Chat", back_populates="founder")
