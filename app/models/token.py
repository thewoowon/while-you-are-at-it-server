from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from app.db.base import Base
from sqlalchemy.orm import relationship


# Token 클래스
class Token(Base):
    __tablename__ = "token"

    # 리프레시 토큰
    refresh_token = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    is_active = Column(Boolean, default=True)

    # 관계 설정
    user = relationship("User", back_populates="tokens")
