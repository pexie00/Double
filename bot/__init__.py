from pyrogram import Client
from logging import getLogger
from logging.config import dictConfig
from .config import Telegram, LOGGER_CONFIG_JSON

dictConfig(LOGGER_CONFIG_JSON)

version = 0.3
logger = getLogger('bot')

TelegramBot = Client(
    name="bot",
    api_id=Telegram.API_ID,
    api_hash=Telegram.API_HASH,
    bot_token=Telegram.BOT_TOKEN,
    plugins={'root': 'bot/plugins'}
)
