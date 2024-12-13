from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Order 클래스
class Order(Base):
    __tablename__ = "order"

    type = Column(String, nullable=False)
    description = Column(String, nullable=False)
    store_id = Column(Integer, ForeignKey("store.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    service_id = Column(Integer, ForeignKey("service.id"))

    # 관계 설정
    user = relationship("User")
    store = relationship("Store")
    service = relationship("Service")
    images = relationship("Image", back_populates="order")
