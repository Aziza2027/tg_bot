from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Namoz🕋'),
            KeyboardButton(text='Sahobalar👳🏻‍♂️️'),
        ],
        [
            KeyboardButton(text='Hadislar📚'),
            KeyboardButton(text='Duo va Zikirlar🤲')
        ],
    ],
    resize_keyboard=True
)