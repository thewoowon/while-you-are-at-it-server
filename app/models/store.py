from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Store 클래스
class Store(Base):
    __tablename__ = "store"

    name = Column(String, index=True)
    address = Column(String, nullable=False)
    type = Column(String, nullable=False)
    business_hours = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
