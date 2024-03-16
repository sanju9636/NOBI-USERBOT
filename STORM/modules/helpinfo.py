from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

INFO_TEXT = f"""
**ɪɴꜰᴏ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}info` » ᴛᴏ ɢᴇᴛ ɪɴꜰᴏ ᴀʙᴏᴜᴛ ʀᴇᴘʟʏᴇᴅ ᴜꜱᴇʀ ᴀᴄᴄ....
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help info"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=INFO_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=INFO_TEXT)
