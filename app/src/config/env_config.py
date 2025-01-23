from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic.types import SecretStr

class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="settings/.env_config", env_file_encoding="utf-8", extra="ignore"
    )

class ProjectConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="project_")

    name: str
    version: str


class OpcUaConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="opcua_")

    host: str
    security: str
    login: SecretStr
    password: SecretStr

class DatabaseConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="db_")

    host: str
    port: int
    login: SecretStr
    password: SecretStr

class FastapiConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="fastapi_")

    host: str
    port: int