from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

hadislarMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Iymon kitobi'),
            KeyboardButton(text='Ilm kitobi'),
        ],
        [
            KeyboardButton(text='Tahorat kitobi'),
            KeyboardButton(text="G'usl kitobi"),
        ],
    ],
    resize_keyboard=True
)