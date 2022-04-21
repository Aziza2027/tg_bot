from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuButton import menu

from loader import dp

@dp.message_handler(Command('menu'))
async def show_menu(msg: Message):
    await msg.answer("salam", reply_markup=menu)