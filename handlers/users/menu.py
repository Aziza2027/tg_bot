from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.sahobalar import sahobalarMenu
from keyboards.default.hadislar import hadislarMenu

from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Tanlang", reply_markup=menu)

@dp.message_handler(text='sahobalar')
async def send_link(message: Message):
    await message.answer("tanlang!",reply_markup=sahobalarMenu)

@dp.message_handler(text='hadislar')
async def send_link(message: Message):
    await message.answer("tanlang!",reply_markup=hadislarMenu)
