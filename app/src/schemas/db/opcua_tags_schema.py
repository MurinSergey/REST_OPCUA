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
    archive: bool
    created_at: datetime
    updated_at: datetime
