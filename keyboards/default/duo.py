from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

duoMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Zikr'),
            KeyboardButton(text='Duo'),
        ],
    ],
    resize_keyboard=True
)