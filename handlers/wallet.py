
import sqlite3

from aiogram import Router, types
from config import bot
from database import sql_queries
from database.a_db import AsyncDatabase


router = Router()

@router.callback_query(lambda call: call.data == "wallet")
async def wallet(call: types.CallbackQuery,
                 db=AsyncDatabase()):

    wallet_user = await db.execute_query(
        query=sql_queries.SELECT_USER_QUERY,
        params=(
            call.from_user.id,
        ),
        fetch='one')
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"your wallet \n"
             f"{wallet_user['ID']}",
    )
    print(wallet_user)


    

