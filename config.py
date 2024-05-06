from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config('TOKEN')
ADMIN_ID = config("ADMIN_ID")
MEDIA_PATH = config("MEDIA_PATH")
bot = Bot(token=TOKEN)
dp = Dispatcher()
