from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

async def like_dislike_keyboard(tg_id):
   like_button = InlineKeyboardButton(
        text="like_ ",
        callback_data=f"like_{tg_id}")

   dislike_button =InlineKeyboardButton(
        text="dislike",
        callback_data=f"dislike{tg_id}",
    )
   markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [like_button],
            [dislike_button]
        ]
    )
   return markup
