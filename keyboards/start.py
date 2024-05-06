from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

async def start_menu_keyboard():
    registration_button = InlineKeyboardButton(
        text="Registration",
        callback_data="registration",)
    profile_button =InlineKeyboardButton(
        text="Profile",
        callback_data="profile",
    )
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [registration_button],
            [profile_button]
        ]
    )
    return markup

