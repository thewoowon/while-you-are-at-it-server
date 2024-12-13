from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from decouple import config

# 데이터베이스 URL (기본적으로 비동기 URL 사용)
DATABASE_URL = config(
    "DATABASE_URL", default="sqlite+aiosqlite:///./app/db/while_you_are_at_it.db")

# 비동기 엔진 및 세션 설정
async_engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

# 동기 엔진 및 세션 설정 (Alembic 전용)
sync_database_url = DATABASE_URL.replace(
    "sqlite+aiosqlite", "sqlite")  # 동기 URL로 변환
sync_engine = create_engine(
    sync_database_url,
    echo=True,
)
SyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=sync_engine
)
