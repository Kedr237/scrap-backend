from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):

    TITLE: str = 'Scrap'
    DOCS_URL: str = '/api/docs'
    OPENAPI_URL: str = '/api/docs.json'

    ROOT_HOST: str = Field(alias='ROOT_HOST')
    ROOT_PORT: str = Field(alias='ROOT_PORT')

    DB_HOST: str = Field(alias='DB_HOST')
    DB_PORT: str = Field(alias='DB_PORT')
    DB_NAME: str = Field(alias='DB_NAME')
    DB_USER: str = Field(alias='DB_USER')
    DB_PASS: str = Field(alias='DB_PASS')

    @property
    def root_url(self) -> str:
        return f'http://{self.ROOT_HOST}:{self.ROOT_PORT}'

    @property
    def db_url(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


@lru_cache
def get_config() -> Config:
    config_instance = Config()
    return config_instance


config = get_config()
