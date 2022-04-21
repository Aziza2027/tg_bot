from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sahobalarMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Abu Bakr As-Siddiq r.a'),
            KeyboardButton(text='Umar ibn Xattob r.a'),
        ],
        [
            KeyboardButton(text='Usmon ibn Affon r.a'),
            KeyboardButton(text='Ali ibn Abu Tolib'),
        ],
    ],
    resize_keyboard=True
)