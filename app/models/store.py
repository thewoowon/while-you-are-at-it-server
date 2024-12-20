from sqlalchemy import Column, String
from app.db.base import Base
from sqlalchemy.orm import relationship


# Store 클래스
class Store(Base):
    __tablename__ = "store"

    name = Column(String, index=True)
    address = Column(String, nullable=False)
    store_type = Column(String, nullable=False)
    business_hours = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    # 관계 설정
    orders = relationship("Order", back_populates="store")
