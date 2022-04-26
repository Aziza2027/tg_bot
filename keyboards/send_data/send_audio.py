from aiogram import types
from aiogram.types import InputFile,Audio

from loader import dp, bot

@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.document.file_id)


@dp.message_handler(text_contains=("Fotiha surasi"))
async def send_surah01(message: types.Message):
    audio_file= InputFile(path_or_bytesio="audio_quran/001_(fotixa).mp3")
    await message.reply_audio(audio_file, caption="Fotiha surasi")

# @dp.message_handler(text_contains=("Baqara surasi"))
# async def send_surah02(message: types.Message):
#     audio_file= InputFile(path_or_bytesio="audio_quran/002(baqara).mp3")
#     audio_url = "https://azan.kz/audio/download/3480"
#     await bot.send_audio(audio_url)
#     #await message.reply_document(audio_file, caption="Baqara surasi")

