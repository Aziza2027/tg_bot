from data.config import BOT_TOKEN
from aiogram.types import Message
from aiogram import types,Bot
from keyboards.inline.namozVaqti import namozVaqtInline
from keyboards.default.menuKeyboard import menu
from loader import dp

bot = Bot(BOT_TOKEN)

@dp.message_handler(text_contains='Namoz vaqtlari🕔')
async def show_menu(message: Message):
    await message.answer('a',reply_markup=namozVaqtInline)

@dp.message_handler()
async def callback(msg: types.Message):
    if msg.text == 'Bosh menu⬅️':
        await bot.send_message(msg.from_user.id,'Bosh menu⬅️',reply_markup=menu)
