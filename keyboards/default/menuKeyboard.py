from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Sahobalar'),
            KeyboardButton(text='hadislar'),
        ],
    ],
    resize_keyboard=True
)