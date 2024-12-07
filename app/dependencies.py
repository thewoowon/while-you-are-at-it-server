# app/dependencies.py
from typing import AsyncGenerator
from app.db.session import SessionLocal


async def get_db() -> AsyncGenerator:
    async with SessionLocal() as session:
        yield session
