from ..repositories.db import opcua_tags_repository
from .db_sqlalchemy_service import DbSqlAlchemyService
from ..schemas.db.opcua_tags_schema import SOpcuaTagCreate, SOpcuaTagUpdate, SOpcuaTagResponse


class DbOpcuaTagsService(DbSqlAlchemyService[SOpcuaTagCreate, SOpcuaTagUpdate, SOpcuaTagResponse]):

    async def create(self, model: SOpcuaTagCreate) -> SOpcuaTagResponse:
        try:
            res = await super().create(model)
            print(f">>>>>Новый тег {model.tag_name} успешно добавлен")
            return res
        except Exception:
            print(f">>>>>Ошибка добавления тега {model.tag_name}")
            raise Exception()
    
    async def update(self, model: SOpcuaTagUpdate, tag_name) -> SOpcuaTagResponse:
        try:
            res = await super().update(model, tag_name=tag_name)
            print(f">>>>>Тег {tag_name} успешно перезаписан под именем {res.tag_name}")
            return res
        except Exception:
            print(f">>>>>Ошибка изменения тега {tag_name}")
            raise Exception()
        
    async def delete(self, tag_name) -> SOpcuaTagResponse:
        res = await super().delete(tag_name=tag_name)
        print(f">>>>>Тег {res.tag_name} успешно удален")
        return res

    async def get_single(self, tag_name) -> SOpcuaTagResponse:
        res = await super().get_single(tag_name=tag_name)
        print(f">>>>>Тег {res.tag_name} успешно получен из базы")
        return res
        
    async def get_all(self) -> list[SOpcuaTagResponse]:
        res = await super().get_all()
        print(f">>>>>Успешно получен список тегов")
        return res


db_opcua_tags_service = DbOpcuaTagsService(repo=opcua_tags_repository)