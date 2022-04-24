from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.booksKeyboard import booksMenu

from loader import dp

@dp.message_handler(text='kitoblar')
async def send_books(message: Message):
    await message.answer("tanlang!",reply_markup=booksMenu)