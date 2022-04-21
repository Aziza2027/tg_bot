from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Sahobalar'),
            KeyboardButton(text='Sahobalar1'),
        ],
    ],
    resize_keyboard=True
)