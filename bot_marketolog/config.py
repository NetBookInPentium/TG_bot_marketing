from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
import logging

storage = MemoryStorage()

class Settings(BaseSettings):
    bot_token: SecretStr
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

config = Settings()

logging.basicConfig(level=logging.INFO, format= "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot, storage=storage)