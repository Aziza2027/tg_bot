from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot

@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def get_file_id_p(message: types.Message):
    await message.reply(message.document.file_id)


@dp.message_handler(text_contains=("Vijdon azobi"))
async def send_book01(message: types.Message):
    book_file = InputFile(path_or_bytesio="books/Vijdon azobi.pdf")
    await message.reply_document(book_file, caption="Vijdon azobi")

@dp.message_handler(text_contains=("Jannatga eltuvchi amallar"))
async def send_book02(message: types.Message):
    book_file = InputFile(path_or_bytesio="books/Жаннатга элтувчи амаллар.pdf")
    await message.reply_document(book_file, caption="Jannatga eltuvchi amallar")

@dp.message_handler(text_contains=("Iymon"))
async def send_book03(message: types.Message):
    book_file = InputFile(path_or_bytesio="books/Муҳаммад_Содиқ_Муҳаммад_Юсуф_Иймон.pdf")
    await message.reply_document(book_file, caption="Muhammad Sodiq Muhammad Yusufning Iymon kitobi")

@dp.message_handler(text_contains=("Tarixi Muhammadiy"))
async def send_book04(message: types.Message):
    book_file = InputFile(path_or_bytesio="books/Alixonto'ra Sog'uniy. Tarixi Muhammadiy.pdf")
    await message.reply_document(book_file, caption="Jannatga eltuvchi amallar")

@dp.message_handler(text_contains=("Ibodati islomiya "))
async def send_book05(message: types.Message):
    book_file = InputFile(path_or_bytesio="books/ibodati_islomiya_ziyouz_com.pdf")
    await message.reply_document(book_file, caption="Ibodati islomiya ")

@dp.message_handler(text_contains=("Qiyomat va Oxirat"))
async def send_book06(message: types.Message):
    book_file = InputFile(path_or_bytesio="books/Imom G'azzoliy. Qiyomat va Oxirat.pdf")
    await message.reply_document(book_file, caption="Qiyomat va Oxirat")

@dp.message_handler(text_contains=("Oisha roziyallohu anhu"))
async def send_book07(message: types.Message):
    book_file = InputFile(path_or_bytesio="books/Oisha roziyallohu anhu.pdf")
    await message.reply_document(book_file, caption="Oisha roziyallohu anhu")

@dp.message_handler(text_contains=("Payg'ambarlar tarixi"))
async def send_book08(message: types.Message):
    book_file = InputFile(path_or_bytesio="books/Payg'ambarlar tarixi.pdf")
    await message.reply_document(book_file, caption="Payg'ambarlar tarixi")

@dp.message_handler(text_contains=("Musulmonning odobi"))
async def send_book09(message: types.Message):
    book_file = InputFile(path_or_bytesio="books/Zohidjon Islomov. Musulmonning odob kitobi.pdf")
    await message.reply_document(book_file, caption="Musulmonning odobi")

@dp.message_handler(text_contains=("Saodat asri(4 tom)"))
async def send_book09(message: types.Message):
    book_file = InputFile(path_or_bytesio="books/Ahmad Lutfiy Qozonchi. Saodat asri qissalari. 1-kitob.pdf")
    await message.answer_document(book_file)
    book_file = InputFile(path_or_bytesio="books/Ahmad Lutfiy Qozonchi. Saodat asri qissalari. 2-kitob.pdf")
    await message.answer_document(book_file)
    book_file = InputFile(path_or_bytesio="books/Ahmad Lutfiy Qozonchi. Saodat asri qissalari. 3-kitob.pdf")
    await message.answer_document(book_file)
    book_file = InputFile(path_or_bytesio="books/Ahmad Lutfiy Qozonchi. Saodat asri qissalari. 4-kitob.pdf")
    await message.answer_document(book_file, caption="Musulmonning odobi")

