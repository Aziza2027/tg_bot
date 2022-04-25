from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random


api_id = 13454428
api_hash = "4a0f506cf1d950e45e0af738bf40cc04"

app = Client("my_account", api_id=api_id, api_hash=api_hash)



@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)


# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0

    while (perc < 100):
        try:
            text = "👮‍ Akhrorova Dilsora! sizning yuragingiz zapt etilmoqda ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🟢 👽 Hayotingizdagi barcha yomon xotiralar o'chirilmoqda")
    sleep(3)

    msg.edit("👽 Hayotingizdagi barcha xotiralar o'chirildi ...")
    perc = 3

    while (perc < 100):
        try:
            text = " Siz Asadbekni yoqtirib qolmoqdasiz ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 5)
            sleep(0.15)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("Akhrorova Dilsora! Siz bir umirga Ismailova bo'lishga rozimisiz :)!")


@app.on_message(filters.command("thanos", prefixes=".") & filters.me)
def thanos(_, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]

    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]

    random.shuffle(members)

    app.send_message(chat, "Щелчок Таноса ... *щёлк*")

    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.x, "seconds.")
            time.sleep(e.x)

    app.send_message(chat, "Но какой ценой?")



app.run()