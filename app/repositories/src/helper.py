from .sqlalchemy_repository import SqlAlchemyRepository
from .list_repository import ListRepository
from ...models.db.tables.opcua_tags_model import OpcuaTagModel
from ...models.opcua.tables.opcua_current_value_model import OpcuaCurrentValue
from ...schemas.db import SOpcuaTagCreate
from ...schemas.opcua import SOpcuaCurrentValueCreate
from ...config.db.db_helper import async_session_maker
from ...config.opcua.opcua_helper import monitored_items

db_opcua_tags_repository = SqlAlchemyRepository[OpcuaTagModel, SOpcuaTagCreate](model=OpcuaTagModel, db_session=async_session_maker)

opcua_current_value_repository = ListRepository[OpcuaCurrentValue, SOpcuaCurrentValueCreate](model=OpcuaCurrentValue, db_list=monitored_items)