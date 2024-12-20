import sys
import os

# 프로젝트 루트를 Python 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.db.base import Base
from app.db.session import sync_engine

# Alembic Config 객체
config = context.config

# Python 로깅 설정
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# SQLAlchemy 메타데이터 (모델 참조)
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Offline 모드에서 마이그레이션 실행."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Online 모드에서 마이그레이션 실행."""
    connectable = sync_engine  # 동기 엔진 사용

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
