from datetime import datetime
from pydantic import BaseModel


class SOpcuaCurrentValueCreate(BaseModel):
    tag_name: str
    opcua_node: str

class SOpcuaCurrentValueResponse(SOpcuaCurrentValueCreate):
    created_at: datetime
    updated_at: datetime
    status_code: str
    status_str: str
    current_value: str
 