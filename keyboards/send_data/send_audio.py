from aiogram import types
from aiogram.types import InputFile

from loader import dp

@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.document.file_id)


@dp.message_handler(text_contains=("001"))
async def send_book01(message: types.Message):
    audio_file= InputFile(path_or_bytesio="audio_quran/001_(fotixa).mp3")
    await message.reply_document(audio_file, caption="Fotiha surasi")