import random
import re
import sqlite3

import random
import re
import sqlite3

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile

from config import bot, ADMIN_ID, MEDIA_PATH
from const import USER_PROFILE, PROFILE_TEXT
from database import sql_queries
from database.a_db import AsyncDatabase
from keyboards.like_dislike import like_dislike_keyboard
from keyboards.profile import my_profile_keyboard
from keyboards.start import start_menu_keyboard

router = Router()


@router.callback_query(lambda call: call.data == "profile")
async def random_profiles_call(call: types.CallbackQuery,
                               db=AsyncDatabase()):
    profile = await db.execute_query(
        query=sql_queries.SELECT_PROFILE_QUERY,
        params=(
            call.from_user.id,
        ),
        fetch='one'
    )
    print(profile)
    if profile:
        photo = types.FSInputFile(profile["PHOTO"])
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=PROFILE_TEXT.format(
                nickname=profile['NICKNAME'],
                password=profile['PASSWORD'],
                data_of_birthday=profile['DATA_OF_BIRTHDAY'],
                bio=profile['BIO'],
            ),
            reply_markup=await my_profile_keyboard()
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="U have not registered ‼️"
        )

@router.callback_query(lambda call: call.data == "delete_profile")
async def delete_profiles_call(call: types.CallbackQuery,
                               db=AsyncDatabase()):
    await db.execute_query(
        query=sql_queries.DEL_MY_PROFILE,
        params=(
            call.from_user.id,
        )
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="your profile has been deleted",
    )
    print(delete_profiles_call)
  #  await bot.