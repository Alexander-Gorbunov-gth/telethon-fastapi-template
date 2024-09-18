from functools import lru_cache
from venv import logger
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import final


@final
class Settings(BaseSettings):
    logger.info("test")
    model_config = SettingsConfigDict(
        env_file=(
            '.dev.env',
            '.env'
        ),  # first search .dev.env, then .prod.env
        env_file_encoding='utf-8',
    )
    debug: bool
    db_url: str
    admin_tg_id: int
    secret_key_jwt: str
    algorythm_jwt: str
    superuser_key: str
    api_id: str
    api_hash: str
    tg_chat_for_log: int



@lru_cache()  # get it from memory
def get_settings() -> Settings:
    logger.debug("get_settings")
    logger.debug(Settings())
    return Settings()
