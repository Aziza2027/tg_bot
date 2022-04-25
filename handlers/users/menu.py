from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.sahobalar import sahobalarMenu
from keyboards.default.hadislar import hadislarMenu
from keyboards.default.quranKeyboards import quranMenu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Bosh menu",reply_markup=menu)

@dp.message_handler(text_contains='Sahobalar👳🏻‍♂️️')
async def send_list(message: Message):
    await message.answer("tanlang!",reply_markup=sahobalarMenu)

@dp.message_handler(text_contains='Bosh menu⬅️')
async def back(message: Message):
    await message.answer("Bosh menu",reply_markup=menu)

@dp.message_handler(text='Hadislar📚')
async def send_hadislar(message: Message):
    await message.answer("tanlang!",reply_markup=hadislarMenu)

@dp.message_handler(text='Qur\'on')
async def send_hadislar(message: Message):
    await message.answer("tanlang!",reply_markup=quranMenu)



