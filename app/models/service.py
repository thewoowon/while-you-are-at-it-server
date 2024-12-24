from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Service 클래스
class Service(Base):
    __tablename__ = "service"

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    discount_rate = Column(Integer, nullable=False)
    service_type = Column(String, nullable=False)
    store_id = Column(Integer, ForeignKey("store.id"))

    # 관계 설정
    store = relationship("Store")
    orders = relationship("Order", back_populates="service")
