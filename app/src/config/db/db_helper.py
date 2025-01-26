from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from ...models.db.tables import BaseModel
from ...config import settings

engine = create_async_engine(settings.db.host)

async_session_maker  = async_sessionmaker(engine, expire_on_commit=False)

async def setup_database():
    async with engine.begin() as conn:
        #await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)