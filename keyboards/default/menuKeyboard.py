from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Sahobalar👳🏻‍♂️️'),
            KeyboardButton(text='Hadislar📚'),
        ],
        [
            KeyboardButton(text='Duo va zikirlar'),
            KeyboardButton(text='Namoz'),
        ]

    ],
    resize_keyboard=True
)