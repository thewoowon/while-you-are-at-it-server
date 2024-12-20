from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Order 클래스
class Order(Base):
    __tablename__ = "order"

    description = Column(String, nullable=False)
    order_type = Column(String, nullable=False)
    store_id = Column(Integer, ForeignKey("store.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    service_id = Column(Integer, ForeignKey("service.id", ondelete="CASCADE"))

    # 관계 설정
    user = relationship("User", back_populates="orders")
    store = relationship("Store", back_populates="orders")
    service = relationship("Service", back_populates="orders")
    images = relationship("Image", back_populates="order")
