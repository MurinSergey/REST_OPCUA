from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .db import Base
import asyncio

engine = create_async_engine("sqlite+aiosqlite:///app/db/database.db")

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def get_session():
    async with new_session() as session:
        yield session

if __name__ == "__main__":
    asyncio.run(setup_database())