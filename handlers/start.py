import sqlite3

from aiogram import Router, types
from aiogram.filters import Command

from config import bot, ADMIN_ID
from database import sql_queries
from database.a_db import AsyncDatabase

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
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name}"
    )

@router.message(lambda message: message.text == "oh no i forget my password!?!")
async def admin_start_menu(message: types.Message,
                           db=AsyncDatabase()):
    if int(ADMIN_ID) == message.from_user.id:
        users = await db.execute_query(
            query=sql_queries.SELECT_USER_QUERY,
            fetch="all"
        )
        await bot.send_message(
            chat_id=message.chat.id,
            text="Here your admin.\n"
                 "This is all bot users"
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
