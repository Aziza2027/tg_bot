from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

namozMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Namoz vaqtlari🕔'),
        ],
        [
            KeyboardButton(text='Namoz qoidalari'),
            KeyboardButton(text='Tahorat qoidalari'),
            KeyboardButton(text='Zam suralar'),
        ],
        [
            KeyboardButton(text='Bosh menu⬅️')
        ],
    ],
    resize_keyboard=True
)