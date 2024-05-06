import sqlite3

from aiogram import Router, types
from aiogram.types import FSInputFile

from config import bot
from const import USER_PROFILE
from database import sql_queries
from database.a_db import AsyncDatabase

router = Router()
@router.callback_query(lambda call: call.data == 'profile')
async def profile_cb(call:types.CallbackQuery,
                        db=AsyncDatabase()):

    profile_db = await db.execute_query(
        query=sql_queries.SELECT_PROFILE_QUERY,
        params=(call.from_user.id,),
        fetch='all'
    )
    data = profile_db[0]
    photo = FSInputFile(data["PHOTO"])
    await bot.send_photo(
        chat_id=call.from_user.id,
        photo=photo,
        caption=USER_PROFILE.format(
            nickname=data['NICKNAME'],
            password=data["PASSWORD"],
            data_of_birthday=data["DATA_OF_BIRTHDAY"],
            bio=data["BIO"],
        )

        )
