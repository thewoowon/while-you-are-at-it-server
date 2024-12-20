from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Notification 클래스
class Notification(Base):
    __tablename__ = "notification"

    title = Column(String, nullable=False)
    contents = Column(String, nullable=False)
    notification_type = Column(String, nullable=False)
    status = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))

    # 관계 설정
    user = relationship("User", back_populates="notifications")
