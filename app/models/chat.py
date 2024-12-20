from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Article 클래스
class Chat(Base):
    __tablename__ = "chat"

    founder_id = Column(Integer, ForeignKey("user.id", ondelete="SET NULL"))
    attendant_id = Column(Integer, ForeignKey("user.id", ondelete="SET NULL"))

    # 관계 설정
    founder = relationship("User", back_populates="chats")
    attendant = relationship("User")
    messages = relationship("Message", back_populates="chat")
