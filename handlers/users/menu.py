from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.hadislar import hadislarMenu
from keyboards.default.namoz import namozMenu
from keyboards.default.duo import duoMenu

from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Tanlang:", reply_markup=menu)

@dp.message_handler(text='Namoz🕋')
async def send_link(message: Message):
    await message.answer("tanlang!",reply_markup=namozMenu)

@dp.message_handler(text='Sahobalar🤲')
async def send_link(message: Message):
    await message.answer("tanlang!",reply_markup=None)

@dp.message_handler(text='Hadislar📚')
async def send_link(message: Message):
    await message.answer("tanlang!",reply_markup=hadislarMenu)

@dp.message_handler(text='Duo va Zikirlar🤲')
async def send_link(message: Message):
    await message.answer("tanlang!", reply_markup=duoMenu)


