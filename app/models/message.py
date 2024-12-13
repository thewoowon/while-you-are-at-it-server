from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Message 클래스
class Message(Base):
    __tablename__ = "message"

    sender_id = Column(Integer, ForeignKey("user.id"))
    chat_id = Column(Integer, ForeignKey("chat.id"))
    sequence = Column(Integer, nullable=False)
    message = Column(String, nullable=False)

    # 관계 설정
    sender = relationship("User")
    chat = relationship("Chat", back_populates="messages")
