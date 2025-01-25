from typing import Generic, Type
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from .db_base_repository import IAbstractDbRepository
from ...models.db.tables import ModelType, CreateSchemaType, UpdateSchemaType

class SqlAlchemyRepository(IAbstractDbRepository, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

        def __init__(self, model: Type[ModelType], db_session: AsyncSession):
            self._session_factory = db_session
            self.model = model

        #Метод для получения всех записей
        async def get_all(self) -> list[ModelType]:
            async with self._session_factory() as session:
                stms = select(self.model).order_by("id")
                res = await session.execute(stms)
                return res.scalars().all()

        #Метод для получения записи по имени тега
        async def get_single(self, **filters) -> list[ModelType]:
            async with self._session_factory() as session:
                stmt = select(self.model).filter_by(**filters).order_by("id")
                res = await session.execute(stmt)
                return res.scalars().all()
                
        #Медот добавления запсиси в базу
        async def create(self, data: CreateSchemaType) -> ModelType:
            async with self._session_factory() as session:
                stmt = insert(self.model).values(**data).returning(self.model)
                res = await session.execute(stmt)
                await session.commit()
                return res.scalar_one()
            
        #Метод для обновления запсиси в базе
        async def update(self, data: UpdateSchemaType, **filters) -> ModelType:
            async with self._session_factory() as session:
                stmt = update(self.model).values(**data).filter_by(**filters).returning(self.model)
                res = await session.execute(stmt)
                await session.commit()
                return res.scalar_one()

        #Метод для удаления записи запсиси в базе
        async def delete(self, **filters) -> ModelType | None:
            async with self._session_factory() as session:
                stmt = delete(self.model).filter_by(**filters).returning(self.model)
                res =  await session.execute(stmt)             
                await session.commit()
                return res.scalar_one()


            

            