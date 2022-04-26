import asyncio
import aioschedule
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from data.config import BOT_TOKEN
from aiogram.utils import executor
import datetime

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)



def time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M")

print(time())


# async def show_menu(message: Message):
#     await bot.send_message(message.from_user.id,'TIME')
#
# async def scheduler():
#     aioschedule.every().day.at("15:03").do(show_menu())
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)
#
# async def on_startup(_):
#     asyncio.create_task(scheduler())
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=False, on_startup=on_startup)