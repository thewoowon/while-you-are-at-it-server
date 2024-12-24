from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.chat import Chat


# User 클래스 -> 대부분 모든 객체가 User 클래스를 사용
class User(Base):
    __tablename__ = "user"

    # 일반 필드
    name = Column(String, nullable=False)
    nickname = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=True)
    src = Column(String, nullable=True)

    # 관계 설정
    orders = relationship("Order", back_populates="user")
    articles = relationship("Article", back_populates="user")
    notifications = relationship("Notification", back_populates="user")

    # User가 생성한 채팅방 (founder)
    created_chats = relationship(
        "Chat",
        back_populates="founder",
        foreign_keys=[Chat.founder_id]  # 문자열이 아닌 컬럼 객체
    )

    # User가 참여한 채팅방 (attendant)
    attended_chats = relationship(
        "Chat",
        back_populates="attendant",
        foreign_keys=[Chat.attendant_id]  # 문자열이 아닌 컬럼 객체
    )
