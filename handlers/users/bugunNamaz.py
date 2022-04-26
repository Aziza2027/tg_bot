from loader import dp, bot
from aiogram.types import Message, CallbackQuery
from data.dataNamaz import times
import datetime

now = datetime.datetime.now()
day = now.strftime('%d')
def bugun():
    for dt in times:
        if dt[0] == day:
            return dt[1]+'\n'+dt[2]+'\n'+dt[4]+'\n'+dt[5]+'\n'+dt[6]+'\n'+dt[7]

@dp.callback_query_handler(text='bugun')
async def inline_today(call: CallbackQuery):
    today = str(bugun())
    await bot.send_message(chat_id=call.from_user.id, text=today)
    await call.answer(cache_time=30)





