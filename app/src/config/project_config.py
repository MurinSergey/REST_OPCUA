from typing_extensions import Annotated
from pydantic_settings import BaseSettings
from pydantic import Field
from .env_config import ProjectConfig, OpcUaConfig, DatabaseConfig, FastapiConfig

class Config(BaseSettings):
    project: Annotated[ProjectConfig, Field(default_factory=ProjectConfig)]
    opcua: Annotated[OpcUaConfig, Field(default_factory=OpcUaConfig)]
    db: Annotated[DatabaseConfig, Field(default_factory=DatabaseConfig)]
    fastapi: Annotated[FastapiConfig, Field(default_factory=FastapiConfig)]

    @classmethod
    def load(cls) -> "Config":
        return cls()
    
settings = Config()