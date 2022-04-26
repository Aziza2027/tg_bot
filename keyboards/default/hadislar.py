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
        [
            KeyboardButton(text='Ilm kitobi'), #17
        ],
        [
            KeyboardButton(text='Tahorat kitobi'), #34
        ],
        [
            KeyboardButton(text="G'usl kitobi"), #54
        ],
        [
            KeyboardButton(text='Hayz kitobi'), #62
        ],
        [
            KeyboardButton(text='Tayammum kitobi'), #70
        ],
        [
            KeyboardButton(text='Namoz kitobi'), #75
        ],
        [
            KeyboardButton(text='Namoz vaqtlari'), #109
            KeyboardButton(text='Nafl namozi'), #230
        ],
        [
            KeyboardButton(text='Juma namozi'), #172
            KeyboardButton(text='Tahajjud namozi'), #221
        ],
        [
            KeyboardButton(text='Juma namozi'),
        ],# sajda oyati #212, qasr namozi #215,
            # makka va madina masjidlarida o'qiladigan namoz #233, namozdagi harakatlar #235, taroveh kitobi #395,
        [
            KeyboardButton(text='Azon kitobi'), #122
        ],
        [
            KeyboardButton(text='Hayit haqida kitob'), #186
        ],
        [
            KeyboardButton(text='Kun tutilishi haqida'), #205
        ],
        [
            KeyboardButton(text='Janoza haqida'), #245
        ],
        [
            KeyboardButton(text="Zakotning vojibligi"), #279
        ],
        [
            KeyboardButton(text='Haj kitobi'), #305 # haj vaqtidagi ov,
        ],
        [
            KeyboardButton(text='Umra haqida'), #351
        ],
        [
            KeyboardButton(text='Madina fazilatlari kitobi'), #370
        ],
        [
            KeyboardButton(text="Ro'za"), #374
        ],
        [
            KeyboardButton(text='Bosh menu⬅️'),
        ],
    ],
    resize_keyboard=True
)