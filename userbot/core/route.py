from typing import Annotated

from fastapi import APIRouter, Header, Depends
from loguru import logger

from telethon import TelegramClient

from config.settings import get_settings

from .bot import get_userbot

cfg = get_settings()

root_router = APIRouter(
    prefix="",
    tags=["root"],
    responses={404: {"description": "Not found"}},
)


@root_router.get("/")
async def root(userbot: TelegramClient = Depends(get_userbot)) -> dict:
    await userbot.send_message("me", message="test1")
    return {"message": "Hello World"}

