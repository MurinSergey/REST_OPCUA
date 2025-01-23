from pydantic_settings import BaseSettings, TomlConfigSettingsSource
from pydantic import Field
from .env_config import ProjectConfig, OpcUaConfig, DatabaseConfig, FastapiConfig

class Config(BaseSettings):
    project: ProjectConfig = Field(default_factory=ProjectConfig)
    opcua: OpcUaConfig = Field(default_factory=OpcUaConfig)
    db: DatabaseConfig = Field(default_factory=DatabaseConfig)
    fastapi: FastapiConfig = Field(default_factory=FastapiConfig)

    @classmethod
    def load(cls) -> "Config":
        return cls()
    
settings = Config()