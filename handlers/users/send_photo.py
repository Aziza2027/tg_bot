from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(text_contains=("Abu Bakr As-Siddiq r.a"))
async def send_photo01(message: types.Message):
    photo_file = InputFile(path_or_bytesio="photos/sahoba01.jpg")
    await message.reply_photo(photo_file, caption="Abu Bakr As-Siddiq (573-634)Abu Bakrga 'As-Siddiq' (Haqiqatni tasdiqlovchi) unvoni berildi. \n "
                                                  "U Muhammad (Sollollohu Alayhi Vasallam)dan ikki yarim yosh kichik va erkaklar orasida birinchi bo'lib Islomga kirgan inson edi. \n"
                                                  "U har doim Muhammad (Sollollohu Alayhi Vasallam.)ning juda yaqin hamrohi bo'lgan. Va u Rasulullohni boshqa odamlardan ko'ra yaxshiroq bilar edi.")

@dp.message_handler(text_contains=("Umar ibn Xattob r.a"))
async def send_photo01(message: types.Message):
    photo_file = InputFile(path_or_bytesio="photos/sahoba02.jpg")
    await message.reply_photo(photo_file, caption="Abu Bakr As-Siddiq r.a haqida")

@dp.message_handler(text_contains=("Usmon ibn Affon r.a"))
async def send_photo01(message: types.Message):
    photo_file = InputFile(path_or_bytesio="photos/sahoba03.jpg")
    await message.reply_photo(photo_file, caption="Abu Bakr As-Siddiq r.a haqida")

@dp.message_handler(text_contains=("Ali ibn Abu Tolib r.a"))
async def send_photo01(message: types.Message):
    photo_file = InputFile(path_or_bytesio="photos/sahoba04.jpg")
    await message.reply_photo(photo_file, caption="Abu Bakr As-Siddiq r.a haqida")

