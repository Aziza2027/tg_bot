from aiogram import types
from data.config import ADMINS
from loader import dp

@dp.message_handler(chat_id=ADMINS, commands='admin')
async def admins_command(msg: types.Message):
    await msg.answer('Salom Admin')