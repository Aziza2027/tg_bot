from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.booksKeyboard import booksMenu
from keyboards.default.quranKeyboards import quranMenu

from loader import dp

@dp.message_handler(text='kitoblar')
async def send_books(message: Message):
    await message.answer("tanlang!",reply_markup=booksMenu)

@dp.message_handler(text='Qur\'on')
async def send_books(message: Message):
    await message.answer("tanlang!",reply_markup=quranMenu)