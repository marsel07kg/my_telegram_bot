from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config
from aiogram.client.session.aiohttp import AiohttpSession

storage = MemoryStorage()
TOKEN = config("TOKEN")
ADMIN_ID = config("ADMIN_ID")
MEDIA_PATH = config("MEDIA_PATH")
bot = Bot(token=TOKEN)
dp = Dispatcher()
