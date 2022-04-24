from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Qur\'on'),
        ],
        [
            KeyboardButton(text='Sahobalar👳🏻‍♂️️'),
            KeyboardButton(text='Hadislar📚'),
        ],
        [
            KeyboardButton(text='Duo va zikirlar'),
            KeyboardButton(text='Namoz'),
        ],
        [
            KeyboardButton(text='kitoblar'),
        ],

    ],
    resize_keyboard=True
)