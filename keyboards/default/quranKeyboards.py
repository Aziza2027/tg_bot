from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

quranMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Fotiha surasi'),
            KeyboardButton(text='Baqara surasi'),
        ],
    ],
    resize_keyboard=True
)