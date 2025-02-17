from .sqlalchemy_service import SqlAlchemyService
from ...repositories import db_opcua_tags_repository
from ...schemas.db import SOpcuaTagCreate, SOpcuaTagResponse

db_opcua_tags_service = SqlAlchemyService[SOpcuaTagCreate, SOpcuaTagResponse](repo=db_opcua_tags_repository)