import sqlite3

from aiogram import Router, types
from aiogram.filters import Command

from config import bot, ADMIN_ID, MEDIA_PATH
from database import sql_queries
from database.a_db import AsyncDatabase
from const import START_MENU_TEXT
from keyboards.start import start_menu_keyboard
router = Router()


@router.message(Command("start"))
async def start_menu(message: types.Message,
                     db=AsyncDatabase()):
    print(message)
    await db.execute_query(
        query=sql_queries.INSERT_USER_QUERY,
        params=(
            None,
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name
        ),
        fetch='none'
    )
    animation_file = types.FSInputFile(MEDIA_PATH + "cute_robot.gif")
    await bot.send_animation(
        chat_id=message.from_user.id,
        animation=animation_file,
        caption=START_MENU_TEXT.format(
        user=message.from_user.first_name
        ),
        reply_markup=await start_menu_keyboard(),

    )

@router.message(lambda message: message.text == "oh no i forget my password!?!")
async def admin_start_menu(message: types.Message,
                           db=AsyncDatabase()):
    if int(ADMIN_ID) == message.from_user.id:
        users = await db.execute_query(
            query=sql_queries.SELECT_USER_QUERY,
            fetch="all"
        )
        for user in users:
            await bot.send_message(
            chat_id=message.chat.id,
            text=f"{user}"
            )

    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="who are you?"
        )
