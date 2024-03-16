import heroku3

from os import getenv
from config import SUDO_USERS, OWNER_ID, HEROKU_APP_NAME, HEROKU_API_KEY

from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.user(OWNER_ID) & filters.command(["addsudo"], ["."]))
async def add_sudo(_, message: Message):
       if not message.reply_to_message:
              await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ 🙂")
              return
       elif HEROKU_APP_NAME is None:
              await message.reply_text("[HEROKU]:" "\nPlease Setup Your HEROKU_APP_NAME")
              return
       elif HEROKU_API_KEY is None:
              await message.reply_text("[HEROKU]:" "\nPlease Setup Your **HEROKU_API_KEY")
              return
       else:
              heroku = heroku3.from_key(HEROKU_API_KEY)
              app = heroku.app(HEROKU_APP_NAME)

       ok = await message.reply_text(f"ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ ⏳...")
       heroku_var = app.config()

       sudousers = getenv("SUDO_USERS")
       target = message.reply_to_message.from_user.id
       if sudousers:
           if len(sudousers) > 0:
                  newsudo = f"{sudousers} {target}"
           else:
                  newsudo = f"{target}"
       else:
            newsudo = f"{target}"
       await ok.edit(f"ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ `{target}`\nʀᴇsᴛᴀʀᴛɪɴɢ ⏳...")
       heroku_var["SUDO_USERS"] = newsudo
