from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Namoz🕋'),
            KeyboardButton(text='Qur\'on'),
            KeyboardButton(text='Duo va Zikirlar🤲')
        ],
        [
            KeyboardButton(text='Sahobalar👳🏻‍♂️️'),
            KeyboardButton(text='Hadislar📚'),
            KeyboardButton(text='kitoblar'),
        ],
    ],
    resize_keyboard=True
)