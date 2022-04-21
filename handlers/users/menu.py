from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu

from loader import dp


@dp.message_handlers(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Tanlang", reply_markup=menu)
