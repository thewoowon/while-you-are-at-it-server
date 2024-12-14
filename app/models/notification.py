from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Notification 클래스
class Notification(Base):
    __tablename__ = "notification"

    title = Column(String, nullable=False)
    contents = Column(String, nullable=False)
    notification_type = Column(String, nullable=False)
