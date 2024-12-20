from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Image 클래스
class Image(Base):
    __tablename__ = "image"

    url = Column(String, nullable=False)
    image_type = Column(String, nullable=False)
    order_id = Column(Integer, ForeignKey("order.id", ondelete="CASCADE"))

    # 관계 설정
    order = relationship("Order", back_populates="images")
