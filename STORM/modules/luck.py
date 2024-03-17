import random
from pyrogram import Client, filters
from config import SUDO_USERS

hl = "."

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["luck"], [hl]))
async def luck(client, message):
    if hl + "luck " in message.text:
        text = message.text.split(hl + "luck ", maxsplit=1)[1]
        score = ["1 \n 🍀", "2 \n 🍀", "-1 \n 💩", "-5 \n 💩", "-10 \n 💩", "100 \n 🍀", "-99 \n 💩", "-100 \n 💩", "-10000 \n 💩", "-50 \n 💩"]
        luck_score = random.choice(score)
        await message.reply(f"**{text}**\n\n**ʟᴜᴄᴋ**: **{luck_score}** %\n**")
    else:
        await message.reply("ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ꜰᴏʀᴍᴀᴛ. ᴘʟᴇᴀꜱᴇ ᴜꜱᴇ `.luck` <ʏᴏᴜʀ ɴᴀᴍᴇ>")
