from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Article 클래스
class Chat(Base):
    __tablename__ = "chat"

    founder_id = Column(Integer, ForeignKey("user.id", ondelete="SET NULL"))
    attendant_id = Column(Integer, ForeignKey("user.id", ondelete="SET NULL"))

    # 관계 설정: foreign_keys에 실제 컬럼 객체 사용
    founder = relationship(
        "User",
        back_populates="created_chats",
        foreign_keys=[founder_id]  # 문자열이 아닌 컬럼 객체
    )
    attendant = relationship(
        "User",
        back_populates="attended_chats",
        foreign_keys=[attendant_id]  # 문자열이 아닌 컬럼 객체
    )
    messages = relationship("Message", back_populates="chat")
