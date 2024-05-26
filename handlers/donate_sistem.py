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
class sendmoney(StatesGroup):
    id = State()
    donate = State()

@router.callback_query(lambda call:call.data == 'donate')
async def start_state(call: types.CallbackQuery,
                      state: FSMContext):
    await bot.send_message(call.from_user.id,
                           text='send wallet number')
    await state.set_state(sendmoney.id)

@router.message(sendmoney.id)
async def process_id(message: types.Message,
                     state: FSMContext,
                     db=AsyncDatabase()):
    user = await db.execute_query(
        query=sql_queries.SELECT_ID_QUERY,
        params=(int(message.text),),
        fetch='one'
    )
    if user:
        await state.update_data(id=int(message.text))
        await bot.send_message(message.from_user.id,
                               text='how much do you want to send')
        await state.set_state(sendmoney.donate)

    else:
        await bot.send_message(message.from_user.id,
                               text='no user wit this wallet')

@router.message(sendmoney.donate)
async def process_donate(message: types.Message,
                         state: FSMContext,
                         db=AsyncDatabase()):
    money=int(message.text)
    balance=await db.execute_query(
        query=sql_queries.SELECT_BALANCES_QUERY,
        params=(message.from_user.id,),
        fetch='one')
    balance=balance['COALESCE (BALANCE, 0)']

    if money <= balance:
        await db.execute_query(
            query=sql_queries.UPDATE_SENDER_BALANCE_QUERY,
            params=(money,message.from_user.id,)
        )
        data=await state.update_data()
        await db.execute_query(
            query=sql_queries.UPDATE_USER_BALANCE_QUERY_ID,
            params=(money,data['id'])
        )
        user=await db.execute_query(
            query=sql_queries.SELECT_TG_ID_BY_ID,
            params=(data['id'],),
            fetch='one'
        )
        tg_id=user['TELEGRAM_ID']
        await bot.send_message(chat_id=tg_id,
                               text=f'user{message.from_user.first_name} sent u {money}')

        await bot.send_message(
            chat_id=message.from_user.id,
            text='successfully sent'
        )
        await db.execute_query(
            query=sql_queries.INSERT_WALLET_TRANSACTION,
            params=(None,
                    message.from_user.id,
                    tg_id,
                    money)
        )
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'u dont have enough money\n'
                                    f'ur balance: {balance}')
