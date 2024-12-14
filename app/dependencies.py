from typing import Generator
from sqlalchemy.orm import Session
from app.db.session import SyncSessionLocal


def get_db() -> Generator[Session, None, None]:
    db = SyncSessionLocal()
    try:
        yield db
    finally:
        db.close()
