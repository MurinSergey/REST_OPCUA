from datetime import datetime
from pydantic import BaseModel


class SOpcuaTagCreate(BaseModel):
    tag_name: str
    opcua_node: str
    archive: bool = False

class SOpcuaTagResponse(SOpcuaTagCreate):
    created_at: datetime
    updated_at: datetime
