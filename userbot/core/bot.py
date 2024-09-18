from loguru import logger

from config.settings import get_settings
from telethon import TelegramClient

cfg = get_settings()

api_id = cfg.api_id
api_hash = cfg.api_hash


async def get_userbot():
    async with TelegramClient("anon", api_id, api_hash) as client:
        yield client


async def start_telegram():
    if cfg.debug:
        logger.debug("First run")
    async with TelegramClient("anon", api_id, api_hash) as client:
        await client.send_message(cfg.tg_chat_for_log, 'Start userbot!')
