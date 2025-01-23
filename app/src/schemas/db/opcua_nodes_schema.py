from pydantic import BaseModel

class OpcuaNodeBase(BaseModel):
    tag_name: str
    nodeID: str