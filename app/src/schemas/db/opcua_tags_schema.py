from datetime import datetime
from pydantic import BaseModel

class SOpcuaTagBase(BaseModel):
    tag_name: str
    opcua_node: str

class SOpcuaTagCreate(SOpcuaTagBase):
    pass

class SOpcuaTagUpdate(SOpcuaTagBase):
    archive: bool = False

class SOpcuaTagDelete(SOpcuaTagBase):
    pass

class SOpcuaTagResponse(SOpcuaTagBase):
    id: int
    activated: bool = False
    archive: bool = False
    created_at: datetime
    updated_at: datetime
