from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def reference_menu_keyboard():
    link_button = InlineKeyboardButton(
        text="Link 🔗",
        callback_data=f"reference_link"
    )
    balance_button = InlineKeyboardButton(
        text="Balance 💸",
        callback_data="reference_balance"
    )
    list_reference_button = InlineKeyboardButton(
        text="list reference",
        callback_data="reference_list"
    )
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [link_button],
            [balance_button],
            [list_reference_button],
        ]
    )
    return markup