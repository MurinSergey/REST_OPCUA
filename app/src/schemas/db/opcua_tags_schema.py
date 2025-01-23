from pydantic import BaseModel

class SOpcuaTagBase(BaseModel):
    tag_name: str
    opcua_node: str
    activated: bool = False
    #archive: bool = False

class SOpcuaTagAdd(SOpcuaTagBase):
    pass

class SOpcuaTagUpdate(SOpcuaTagBase):
    pass

class SOpcuaTagDelete(SOpcuaTagBase):
    pass

class SOpcuaTagResponse(SOpcuaTagBase):
    id: int