from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import as_declarative, declared_attr
import pkgutil
import importlib
import app.models  # 모델들이 위치한 디렉토리


@as_declarative()
class Base:
    """공통 속성과 테이블 이름 자동 생성을 위한 베이스 클래스"""
    id = Column(Integer, primary_key=True, index=True)  # 기본 키
    created_at = Column(DateTime, default=func.now(), nullable=False)  # 생성 시간
    updated_at = Column(DateTime, default=func.now(),
                        onupdate=func.now(), nullable=False)  # 업데이트 시간

    @declared_attr
    def __tablename__(cls) -> str:
        """테이블 이름 자동 생성 (클래스 이름을 소문자로 사용)"""
        return cls.__name__.lower()


# 모든 모델을 동적으로 로드 (Alembic 연동 시 필요)
def load_all_models():
    """app.models 패키지 아래의 모든 모듈 임포트"""
    for _, module_name, _ in pkgutil.iter_modules(app.models.__path__):
        importlib.import_module(f"app.models.{module_name}")


# Alembic이 자동으로 모든 모델을 인식하도록 설정
load_all_models()
