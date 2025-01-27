from ..sqlalchemy_repository import SqlAlchemyRepository
from ...models.db.tables.opcua_tags_model import OpcuaTagModel
from ...schemas.db.opcua_tags_schema import SOpcuaTagCreate, SOpcuaTagUpdate
from ...config.db.db_helper import async_session_maker

class OpcuaTagsRepository(SqlAlchemyRepository[OpcuaTagModel, SOpcuaTagCreate, SOpcuaTagUpdate]):
    ...

opcua_tags_repository = OpcuaTagsRepository(model=OpcuaTagModel, db_session=async_session_maker)