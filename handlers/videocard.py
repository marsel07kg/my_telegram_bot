import sqlite3

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.deep_linking import create_start_link

from config import bot, ADMIN_ID, MEDIA_PATH
from const import START_MENU_TEXT
from database import sql_queries
from database.a_db import AsyncDatabase
from keyboards.start import start_menu_keyboard
from scraper.news_scraper import NewsScraper
from scraper.videocard import VideoCardScraper

router = Router()



@router.callback_query(lambda call: call.data == "video_card")
async def latest_news_links(call: types.CallbackQuery,):
    scraper = VideoCardScraper()
    data = scraper.scrape_data()
    for video_card in data:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="https://lindeal.com" + video_card
        )