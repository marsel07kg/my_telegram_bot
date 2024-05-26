import sqlite3

from aiogram import Router, types


from config import bot

from scraper.videocard import VideoCardScraper

router = Router()



@router.callback_query(lambda call: call.data == "video_card")
async def video_card_links(call: types.CallbackQuery,):
    scraper = VideoCardScraper()
    data = scraper.scrape_data()
    for video_card in data:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="https://lindeal.com" + video_card
        )