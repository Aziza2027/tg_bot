from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

namozVaqtInline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Bugun', callback_data='bugun'),
            InlineKeyboardButton(text="Obuna bo'lish", callback_data='obuna')
        ],
        [
            InlineKeyboardButton(text='Obunani bekor qilish', callback_data='bekor')
        ],
    ])