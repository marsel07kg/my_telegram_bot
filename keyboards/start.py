from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

async def start_menu_keyboard():
    registration_button = InlineKeyboardButton(
        text="Registration",
        callback_data="registration",)
    my_profile_button =InlineKeyboardButton(
        text="Profile",
        callback_data="profile",
    )
    profiles_button = InlineKeyboardButton(
        text="View Profiles 🧲",
        callback_data="view_profiles")

    reference_button = InlineKeyboardButton(
        text="Reference Menu 💵",
        callback_data="reference_menu"
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [registration_button],
            [my_profile_button],
            [profiles_button],
            [reference_button]
        ]
    )
    return markup

