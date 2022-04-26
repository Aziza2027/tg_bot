from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sahobalarMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Abu Bakr As-Siddiq r.a'),
            KeyboardButton(text='Umar ibn Xattob r.a'),
        ],
        [
            KeyboardButton(text='Usmon ibn Affon r.a'),
            KeyboardButton(text='Ali ibn Abu Tolib r.a'),
        ],
        [
            KeyboardButton(text='Abdurahmon ibn avf'),
            KeyboardButton(text="Abu Ubayda ibn al-Jarroh"),
        ],        [
            KeyboardButton(text='Zubayr ibn avvom'),
            KeyboardButton(text="Talha ibn ubaydulloh"),
        ],
        [
            KeyboardButton(text='saad ibn abu vaqqos'),
            KeyboardButton(text="Said ibn Zayd"),
        ],
        [
            KeyboardButton(text='Bosh menu⬅️'),
        ],

    ],
    resize_keyboard=True
)