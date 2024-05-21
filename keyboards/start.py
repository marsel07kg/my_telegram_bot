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

    wallet_button = InlineKeyboardButton(
        text="your wallet",
        callback_data="wallet"
    )
    like_history_button = InlineKeyboardButton(
        text="Liked Profiles 🩵",
        callback_data="history"
    )
    donate_button = InlineKeyboardButton(
        text="Donate to wallet",
        callback_data="donate"
    )
    news_button = InlineKeyboardButton(
        text="Latest News 🗞️",
        callback_data="news"
    )
    videocard_button = InlineKeyboardButton(
        text="Video card",
        callback_data="video_card"
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [registration_button],
            [my_profile_button],
            [profiles_button],
            [reference_button],
            [wallet_button],
            [like_history_button],
            [donate_button],
            [news_button],
            [videocard_button],
        ]
    )
    return markup

