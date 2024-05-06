import sqlite3

from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile

from config import bot
from const import PROFILE_TEXT
from database import sql_queries
from database.a_db import AsyncDatabase



router = Router()


class RegistrationStates(StatesGroup):
    nickname = State()
    password = State()
    data_of_birthday = State()
    bio = State()
    photo = State()


@router.callback_query(lambda call: call.data == "registration")
async def registration_start(call: types.CallbackQuery,
                             state: FSMContext):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Send me ur Nickname, please!"
    )
    await state.set_state(RegistrationStates.nickname)


@router.message(RegistrationStates.nickname)
async def process_nickname(message: types.Message,
                           state: FSMContext):
    await state.update_data(nickname=message.text)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="create password for profile"
    )
    data = await state.get_data()
    print(data)
    await state.set_state(RegistrationStates.password)


@router.message(RegistrationStates.password)
async def process_password(message: types.Message,
                           state: FSMContext):
    await state.update_data(password=message.text)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="what is your birthday?"
    )
    data = await state.get_data()
    print(data)
    await state.set_state(RegistrationStates.data_of_birthday)


@router.message(RegistrationStates.data_of_birthday)
async def process_data_of_birthday(message: types.Message,
                           state: FSMContext):
    await state.update_data(data_of_birthday=message.text)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Tell me about urself"
    )
    data = await state.get_data()
    print(data)
    await state.set_state(RegistrationStates.bio)


@router.message(RegistrationStates.bio)
async def process_bio(message: types.Message,
                      state: FSMContext):
    await state.update_data(bio=message.text)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Let me look at u, Send me ur Photo"
    )
    data = await state.get_data()
    print(data)
    await state.set_state(RegistrationStates.photo)


@router.message(RegistrationStates.photo)
async def process_photo(message: types.Message,
                        state: FSMContext,
                        db=AsyncDatabase()):
    file_id = message.photo[-1].file_id
    print(message.photo)
    file = await bot.get_file(file_id)
    file_path = file.file_path
    media_final_path = 'media/' + file_path
    await bot.download_file(
        file_path,
        'media/' + file_path
    )
    data = await state.get_data()

    photo = FSInputFile('media/' + file_path)
    try:
        await db.execute_query(
            query=sql_queries.INSERT_PROFILE_QUERY,
            params=(
                None,
                message.from_user.id,
                data['password'],
                data['nickname'],
                data['data_of_birthday'],
                data['bio'],
                'media/' + file_path

            ),
            fetch='none'
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="U have registered before "
        )
        return

    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo,
        caption=PROFILE_TEXT.format(
            nickname=data['nickname'],
            password=data['password'],
            data_of_birthday=data['data_of_birthday'],
            bio=data['bio'],
        )
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text="U have registered successfully "
    )

