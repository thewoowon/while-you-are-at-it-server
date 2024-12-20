from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


# Article 클래스
class Article(Base):
    __tablename__ = "article"

    title = Column(String, nullable=False)
    contents = Column(String, nullable=False)
    article_type = Column(String, nullable=False)
    pick_up_location = Column(String, nullable=False)
    pick_up_time = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    departure_date_and_time = Column(String, nullable=False)
    number_of_recruits = Column(Integer, nullable=False)
    process_status = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))

    # 관계 설정
    user = relationship("User", back_populates="articles")
