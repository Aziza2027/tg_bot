from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Sahobalar'),
            KeyboardButton(text='hadislar'),
        ],
        [
            KeyboardButton(text='Hadislar'),
            KeyboardButton(text='Namoz'),
        ]
    ],
    resize_keyboard=True
)